import socket
import struct
import pickle


class ClientSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.73", port=12345):
        # raspberry pi IP
        self.host = raspberry
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    def connect(self):
        self.client_socket.connect((self.host,self.port))

    # close connection
    def close(self):
        self.client_socket.close()

    # get floats from server
    def get_floats(self, no_floats):
        size = struct.calcsize("f"*no_floats)
        msg = self.client_socket.recv(size)
        print(msg)
        return struct.unpack("!" + "f"*no_floats, self.client_socket.recv(size))

    # send floats to server
    def send_floats(self, floats_list):
        floats_msg = struct.pack("!" + len(floats_list)*"f", *floats_list)
        self.client_socket.sendall(floats_msg)

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
    count = 1
    while True:
        """
        try:
            values_received = client_socket.get_floats(3)
            print(values_received)
        except:
            print("no response from server")
            pass
        """
        try:
            dict_received = client_socket.get_dict(1024)
            print(dict_received, count)
            count += 1
        except:
            pass
    # close the socket
    client_socket.close()







