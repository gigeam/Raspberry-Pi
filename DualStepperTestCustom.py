#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()
st2 = threading.Thread()


# recommended for auto-disabling motors on shutdown
def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

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


def stepper_worker(stepper, num_steps, moving_direction, style):
    # print("Stepping!")
    stepper.step(num_steps, moving_direction, style)
    # print("Done")

while True:
    direction = random.randint(0, 1)
    random_steps = random.randint(50, 100)
    pos_stepstyles = 0
    # Stepper 1
    if not st1.isAlive():
        if direction == 0:
            d = Adafruit_MotorHAT.FORWARD
        else:
            d = Adafruit_MotorHAT.BACKWARD
        print("Stepper 1", "%d steps" % random_steps, "forward" if direction == 0 else "backward")
        st1 = threading.Thread(target=stepper_worker, args=(myStepper1, random_steps, d, stepstyles[pos_stepstyles],))
        st1.start()
    # Stepper 2
    if not st2.isAlive():
        if direction == 0:
            d = Adafruit_MotorHAT.BACKWARD
        else:
            d = Adafruit_MotorHAT.FORWARD
        print("Stepper 2", "%d steps" % random_steps, "forward" if direction == 0 else "backward")
        st2 = threading.Thread(target=stepper_worker, args=(myStepper2, random_steps, d, stepstyles[pos_stepstyles],))
        st2.start()
    # 0.5 small delay to stop from constantly polling threads
    # https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)
    time.sleep(0.5)
