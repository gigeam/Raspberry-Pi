from sense_hat import SenseHat


sense = SenseHat()

# print stuff to LED
"""
blue = (0, 0, 255)
yellow = (255, 255, 0)
while True:
  sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)
"""

# show pitch, roll, yaw
while True:
    orientation = sense.get_orientation()
    print("Pitch %d, Roll %d, Yaw %d" % (orientation["pitch"], orientation["roll"], orientation["yaw"]))
    