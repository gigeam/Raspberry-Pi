from sense_hat import SenseHat
from pynput import keyboard
import pandas as pd


sense = SenseHat()
angles_list = []


# define behaviour for key press
def on_press(key):
    try:
        print("alphanumeric pressed: ", key.char)
        # pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
        orientation = sense.get_orientation()
        angle_info = {"pitch": orientation["pitch"],
                      "roll": orientation["roll"],
                      "yaw": orientation["yaw"],
                      "command": "stop"}
        # change the command depending on what keys are pressed
        if key.char == "f":
            angle_info["command"] = "forward"
            # show value on LED
            sense.show_message("f")
        if key.char == "b":
            angle_info["command"] = "backward"
            # show value on LED
            sense.show_message("b")
        if key.char == "l":
            angle_info["command"] = "left"
            # show value on LED
            sense.show_message("l")
        if key.char == "r":
            angle_info["command"] = "right"
            # show value on LED
            sense.show_message("r")
        # print to screen all the angle_info values
        print("pitch: ", angle_info["pitch"],
              "roll: ", angle_info["roll"],
              "yaw: ", angle_info["yaw"],
              "command: ", angle_info["command"])
        # append angle_info to list
        angles_list.append(angle_info)
    except AttributeError:
        print("special key pressed: ", key)


# define behaviour for key release
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        print("Saving angle_info dataframe...")
        pd.DataFrame(angles_list).to_csv("angle_info.csv", index=False)
        print("Exiting program...")
        # stop listener
        return False

# collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



"""
sense = SenseHat()

# print stuff to LED

# blue = (0, 0, 255)
# yellow = (255, 255, 0)
# while True:
#  sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)


angles_list = []
# show pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
while True:
    orientation = sense.get_orientation()
    angle = {"pitch": orientation["pitch"], "roll": orientation["roll"], "yaw": orientation["yaw"]}

    lis = keyboard.Listener(on_press=on_press)
    lis.start()  # start to listen on a separate thread
    lis.join()   # no this if main thread is polling self.keys

    print("stuff")

    
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
    

"""