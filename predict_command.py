from sense_hat import SenseHat
from sklearn.externals import joblib
from knn_predict import predict_command
import keyboard

# instantiate sense hat object
sense = SenseHat()
# load pre-trained classifier from file
clf = joblib.load('knn_distance.pkl')
# repeat until q is pressed
while True:
    # pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
    orientation = sense.get_orientation()
    # extract the two dimensions i.e. pitch and roll
    angle = [orientation["pitch"], orientation["roll"]]
    angle = [360, 360]
    predict_command(clf, angle)
    # exit the program
    if keyboard.is_pressed("q"):
        print("Exiting program...")
        break
