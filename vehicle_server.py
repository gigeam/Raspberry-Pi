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

    # close connection
    def close(self):
        self.server_socket.close()

    # receive dictionary
    def get_dict(self, size):
        data, address = self.server_socket.recvfrom(size)
        return pickle.loads(data), address


if __name__ == "__main__":
    # create a socket object
    server_socket = ServerSocket()
    print("listening to socket")
    while True:
        print(sys.stderr, '\nwaiting to receive message')
        received_data, sender_address = server_socket.get_dict(4096)

        print(sys.stderr, 'received %s bytes from %s' % (len(received_data), sender_address))
        print(sys.stderr, received_data)
        """
        if data:
            sent = sock.sendto(data, address)
            print(sys.stderr, 'sent %s bytes back to %s' % (sent, address))
        """