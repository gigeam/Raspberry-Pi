from sense_hat import SenseHat

# instantiate a SenseHat object
sense = SenseHat()

# show pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
while True:
    orientation = sense.get_orientation()
    print("Pitch %d, Roll %d, Yaw %d" % (orientation["pitch"], orientation["roll"], orientation["yaw"]))