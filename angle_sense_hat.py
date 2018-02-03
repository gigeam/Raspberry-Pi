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
        # create a dictionary with with the following keys: pitch, roll, yaw, command
        angle_info = {"pitch": orientation["pitch"],
                      "roll": orientation["roll"],
                      "yaw": orientation["yaw"],
                      "command": "stop"}
        # change the command depending on what keys are pressed on the keyboard
        if key.char == "f":
            angle_info["command"] = "forward"
        if key.char == "b":
            angle_info["command"] = "backward"
        if key.char == "l":
            angle_info["command"] = "left"
        if key.char == "r":
            angle_info["command"] = "right"
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
    # when esc key is pressed save list into a dataframe file
    if key == keyboard.Key.esc:
        print("Saving angle_info dataframe...")
        pd.DataFrame(angles_list).to_csv("angle_info.csv", index=False)
        print("Exiting program...")
        # stop listener
        return False

# collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
