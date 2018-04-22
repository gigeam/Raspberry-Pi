# Raspberry-Pi Robotic Vehicle

This project contains the source code behind a robotic vehicle concept comprised of:

 1) A joystick

 Joystick component is using a Raspberry Pi and Sense HAT add-on. It is sensing orientation angle using accelerometer,
 gyroscope and magnetometer. k-nearest neighbour classifier is used to infer a vehicle command which is then sent to
 the vehicle via a WiFi router.

 2) A vehicle

 Vehicle component is using a Raspberry Pi and Adafruit Motor HAT add-on to control two stepper motors according to
 received command from the joystick.