from sense_hat import SenseHat
import keyboard
import pandas as pd


sense = SenseHat()

# print stuff to LED
"""
blue = (0, 0, 255)
yellow = (255, 255, 0)
while True:
  sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)
"""

angles_list = []
# show pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
while True:
    orientation = sense.get_orientation()
    angle = {"pitch": orientation["pitch"], "roll": orientation["roll"], "yaw": orientation["yaw"]}
    if keyboard.is_pressed("f"):
        angle["command"] = "forward"
    elif keyboard.is_pressed("b"):
        angle["command"] = "backward"
    elif keyboard.is_pressed("l"):
        angle["command"] = "left"
    elif keyboard.is_pressed("r"):
        angle["command"] = "right"
    else:
        angle["command"] = "stop"
        
    print("Pitch %d, Roll %d, Yaw %d, Command %s" % (angle["pitch"], angle["roll"], angle["yaw"], angle["command"]))    
    angles_list.append(angle)
    if keyboard.is_pressed("q"):
        print("Saving angle dataframe..")
        pd.DataFrame(angles_list).to_csv("angles.csv", index=False)
        print("Exiting program...")
        break