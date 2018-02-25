import socket
import sys
import pickle


class ClientSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
        # raspberry pi IP
        self.host = raspberry
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # close connection
    def close(self):
        self.client_socket.close()

    # send dictionary to server
    def send_dict(self, dictionary):
        data_p = pickle.dumps(dictionary)
        self.client_socket.sendto(data_p, (self.host, self.port))

# Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server_address = ('localhost', 10000)
# message = 'This is the message.  It will be repeated.'


client_socket = ClientSocket()
try:
    # send data
    # sent = sock.sendto(message.encode(), server_address)
    dict_command = {"command_1": 1, "command_2": 2, "command_3": 3}
    client_socket.send_dict(dict_command)
    # Receive response
    # print(sys.stderr, 'waiting to receive')
    # data, server = sock.recvfrom(4096)
    # print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    client_socket.close()

"""
if __name__ == "__main__":
    # create a socket object
    client_socket = ClientSocket()
    # connect to server
    client_socket.connect()
    print("connected to socket")
    count = 1
    while True:
"""