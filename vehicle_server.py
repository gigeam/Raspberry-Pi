import socket
import sys
import pickle
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random


# create a UDP socket
class ServerSocket(object):
    # constructor method
    def __init__(self, raspberry="192.168.0.86", port=12345):
        self.host = raspberry
        self.port = port
        # https://pymotw.com/2/socket/udp.html
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))

    # close connection
    def close(self):
        self.server_socket.close()

    # receive dictionary
    def get_dict(self, size):
        data, address = self.server_socket.recvfrom(size)
        return pickle.loads(data), address


# recommended for auto-disabling motors on shutdown
def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def stepper_worker(stepper, num_steps, moving_direction, style):
    # print("Stepping!")
    stepper.step(num_steps, moving_direction, style)
    # print("Done")

if __name__ == "__main__":
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT()
    # create empty threads (these will hold the stepper 1 and 2 threads)
    st1 = threading.Thread()
    st2 = threading.Thread()
    atexit.register(turn_off_motors)
    # 200 steps/rev, motor port #1
    myStepper1 = mh.getStepper(200, 1)
    # 200 steps/rev, motor port #2
    myStepper2 = mh.getStepper(200, 2)
    # 100 RPM
    myStepper1.setSpeed(100)
    # 100 RPM
    myStepper2.setSpeed(100)
    # a list with all the possible step styles
    stepstyles = [Adafruit_MotorHAT.SINGLE,
                  Adafruit_MotorHAT.DOUBLE,
                  Adafruit_MotorHAT.INTERLEAVE,
                  Adafruit_MotorHAT.MICROSTEP]
    # create a socket object
    server_socket = ServerSocket()
    print("listening to socket")
    while True:
        print(sys.stderr, '\nwaiting to receive message')
        received_data, sender_address = server_socket.get_dict(4096)
        # print(sys.stderr, 'received %s bytes from %s' % (len(received_data), sender_address))
        print(sys.stderr, received_data)
        # 0 backward, 1 forward
        direction = received_data["command"]
        # assert that a valid command was received
        assert(direction == "stop" or
               direction == "forward" or
               direction == "backward" or
               direction == "left" or
               direction == "right")
        # simply continue if received command was "stop"
        if direction == "stop":
            continue
        no_steps = 20
        pos_stepstyles = 0
        # stepper 1
        if not st1.isAlive():
            if direction == "backward":
                d = Adafruit_MotorHAT.FORWARD
            elif direction == "forward":
                d = Adafruit_MotorHAT.BACKWARD
            elif direction == "left":
                d = Adafruit_MotorHAT.FORWARD
            else:
                d = Adafruit_MotorHAT.BACKWARD
            # start thread with stepper 1
            st1 = threading.Thread(target=stepper_worker, args=(myStepper1, no_steps, d, stepstyles[pos_stepstyles],))
            st1.start()
        # stepper 2
        if not st2.isAlive():
            if direction == "backward":
                d = Adafruit_MotorHAT.BACKWARD
            elif direction == "forward":
                d = Adafruit_MotorHAT.FORWARD
            elif direction == "left":
                d = Adafruit_MotorHAT.FORWARD
            else:
                d = Adafruit_MotorHAT.BACKWARD
            # start thread with stepper 2
            st2 = threading.Thread(target=stepper_worker, args=(myStepper2, no_steps, d, stepstyles[pos_stepstyles],))
            st2.start()
        # 0.01 small delay to stop from constantly polling threads
        # https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)
        time.sleep(0.01)

