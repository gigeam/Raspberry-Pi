import socket
import pickle


class ClientSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
        # raspberry pi IP
        self.host = raspberry
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # connect to server
    def connect(self):
        self.client_socket.connect((self.host, self.port))

    # close connection
    def close(self):
        self.client_socket.close()

    # get dictionary from server
    def get_dict(self, size):
        dict_msg = self.client_socket.recv(size)
        return pickle.loads(dict_msg)

    # send dictionary to server
    def send_dict(self, dictionary):
        data_p = pickle.dumps(dictionary)
        self.client_socket.sendall(data_p)


if __name__ == "__main__":
    # create a socket object
    client_socket = ClientSocket()
    # connect to server
    client_socket.connect()
    print("connected to socket")
    val_1, val_2, val_3 = 1, 2, 3
    while True:
        try:
            command_dictionary = {"command1": val_1, "command2": val_2, "command3": val_3}
            client_socket.send_dict(command_dictionary)
        except:
            pass
        # client_socket.close()
