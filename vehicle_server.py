import socket
import pickle


class ServerSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
        self.host = raspberry
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    # accept connection
    def accept(self):
        return self.server_socket.accept()

    # close connection
    def close(self):
        self.server_socket.close()

    # send dictionary
    @staticmethod
    def send_dict(connection, dictionary):
        data_p = pickle.dumps(dictionary)
        connection.sendall(data_p)

    # receive dictionary
    @staticmethod
    def get_dict(connection, size):
        dict_msg = connection.recv(size)
        return pickle.loads(dict_msg)


if __name__ == "__main__":
    # create a socket object
    server_socket = ServerSocket()
    print("listening to socket")
    connect, address = server_socket.accept()
    print("got connection from", address)
    # val_1, val_2, val_3 = 1, 2, 3
    count = 1
    while True:
        # command_dictionary = {"val1": val_1, "val2": val_2, "val3": val_3}
        # server_socket.send_dict(connect, command_dictionary)
        values_received = server_socket.get_dict(connect, 1024)
        print(values_received, count)
        count += 1
    # close the socket
    server_socket.close()







