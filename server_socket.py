import socket
import pickle
from PIL import Image
import io
import struct


class ServerSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.73", port=12345):
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

    # get an array such as a 1 channel image
    @staticmethod
    def get_image(connection, size):
        # size = array_size.width * array_size.height * array_size.bytes_per_element
        packed_data = connection.recv(size)
        # this is what it would look like for a PNG image
        image = Image.open(io.BytesIO(b"\x89PNG" + packed_data))
        # image.show()
        return image

    # send tuple of floats
    @staticmethod
    def send_floats(connection, floats_list):
        # print(len(floats_list)*"f", *floats_list)
        floats_msg = struct.pack("!" + len(floats_list)*"f", *floats_list)
        connection.sendall(floats_msg)

    # receive tuple of floats
    @staticmethod
    def get_floats(connection, no_floats):
        size = 4 * no_floats
        return struct.unpack("!" + "f"*no_floats, connection.recv(size))
    
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
    con, address = server_socket.accept()
    print("got connection from", address)
    val_1 = 1
    val_2 = 2
    val_3 = 3
    while True:
        # values_sent = [1.0, 2.0, 3.0]
        # server_socket.send_floats(con, values_sent)
        dict = {"val1":val_1, "val2":val_2, "val3":val_3}
        server_socket.send_dict(con, dict)
        # values_received = server_socket.get_floats(con, 3)
        # print(values_received)
    # close the socket
    server_socket.close()







