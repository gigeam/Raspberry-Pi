import socket
import sys
import pickle
import time
from sense_hat import SenseHat
from sklearn.externals import joblib
import numpy as np


# create a UDP client socket
class ClientSocket(object):
    # constructor method
    def __init__(self, raspberry="172.20.10.5", port=12345):
        # raspberry pi IP
        self.host = raspberry
        self.port = port
        # https://pymotw.com/2/socket/udp.html
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # close connection
    def close(self):
        self.client_socket.close()

    # send dictionary to server
    def send_dict(self, dictionary):
        data_p = pickle.dumps(dictionary)
        self.client_socket.sendto(data_p, (self.host, self.port))


# predict command using loaded classifier
def predict_command(knn_clf, input_angle):
    codes = {0: "stop", 1: "forward", 2: "backward", 3: "left", 4: "right"}
    cmd = knn_clf.predict(np.array(input_angle).reshape(1, 2))[0]
    print("command: ", codes[cmd])
    return codes[cmd]

if __name__ == "__main__":
    # instantiate sense hat object
    sense = SenseHat()
    # load pre-trained classifier from file
    clf = joblib.load('knn_uniform.pkl')
    # create a socket object
    client_socket = ClientSocket()
    print("connecting to socket")
    # repeat forever, execution can be stopped using ctrl+c
    while True:
        # pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
        orientation = sense.get_orientation()
        # extract the two dimensions i.e. pitch and roll
        angle = [orientation["pitch"], orientation["roll"]]
        # infer a command using knn classifier
        command = predict_command(clf, angle)
        # send command as a dictionary
        dict_command = {"command": command}
        print(sys.stderr, 'sending "%s"' % dict_command)
        client_socket.send_dict(dict_command)
        # 0.05 small delay between commands
        time.sleep(0.05)
