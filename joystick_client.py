import socket
import sys
import pickle
import time


# create a UDP socket
class ClientSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
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

if __name__ == "__main__":
    # create a socket object
    client_socket = ClientSocket()
    print("connecting to socket")
    while True:
        # send command
        dict_command = {"command": "forward"}
        print(sys.stderr, 'sending "%s"' % dict_command)
        client_socket.send_dict(dict_command)
        time.sleep(0.5)
