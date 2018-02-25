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


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = mh.getStepper(200, 1)      # 200 steps/rev, motor port #1
myStepper2 = mh.getStepper(200, 2)      # 200 steps/rev, motor port #1
myStepper1.setSpeed(120)          # 120 RPM
myStepper2.setSpeed(120)          # 120 RPM


stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")

while (True):
    randomdir = random.randint(0, 1)
    randomsteps = random.randint(10, 50)
    pos_stepstyles = 0
    if not st1.isAlive():
        #randomdir = random.randint(0, 1)
        #print("Stepper 1"),
        if (randomdir == 0):
            dir = Adafruit_MotorHAT.FORWARD
            #print("forward"),
        else:
            dir = Adafruit_MotorHAT.BACKWARD
            #print("backward"),
        #randomsteps = random.randint(10, 50)
        print("Stepper 1", "%d steps" % randomsteps, "forward" if randomdir ==0 else "backward")
        st1 = threading.Thread(target=stepper_worker, args=(myStepper1, randomsteps, dir, stepstyles[pos_stepstyles],))
        st1.start()

    if not st2.isAlive():
        #print("Stepper 2"),
        #randomdir = random.randint(0, 1)
        if (randomdir == 0):
            dir = Adafruit_MotorHAT.BACKWARD
            #print("forward"),
        else:
            dir = Adafruit_MotorHAT.FORWARD
            #print("backward"),

        #randomsteps = random.randint(10, 50)
        print("Stepper 2", "%d steps" % randomsteps, "forward" if randomdir == 0 else "backward")

        st2 = threading.Thread(target=stepper_worker, args=(myStepper2, randomsteps, dir, stepstyles[pos_stepstyles],))
        st2.start()
    
    time.sleep(0.5) #0.1 Small delay to stop from constantly polling threads (see: https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)
