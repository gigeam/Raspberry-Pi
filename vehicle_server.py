import socket
import sys
import pickle


class ServerSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
        self.host = raspberry
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))

    # accept connection
    def accept(self):
        return self.server_socket.accept()

    # close connection
    def close(self):
        self.server_socket.close()

    # receive dictionary
    @staticmethod
    def get_dict(connect, size):
        dict_msg = connect.recvfrom(size)
        return pickle.loads(dict_msg)


if __name__ == "__main__":
    # create a socket object
    server_socket = ServerSocket()
    print("listening to socket")
    connection, address = server_socket.accept()
    print("got connection from", address)
    while True:
        print(sys.stderr, '\nwaiting to receive message')
        data = server_socket.get_dict(connection, 4096)

        print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
        print(sys.stderr, data)
        """
        if data:
            sent = sock.sendto(data, address)
            print(sys.stderr, 'sent %s bytes back to %s' % (sent, address))
        """