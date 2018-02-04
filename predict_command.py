from sense_hat import SenseHat
from sklearn.externals import joblib
from knn_predict import predict_command

# instantiate sense hat object
sense = SenseHat()
# load pre-trained classifier from file
clf = joblib.load('knn_uniform.pkl')
# repeat forever, execution can be stopped using ctrl+c
while True:
    # pitch, roll, yaw, using accelerometer, gyroscope and magnetometer (for best accuracy)
    orientation = sense.get_orientation()
    # extract the two dimensions i.e. pitch and roll
    angle = [orientation["pitch"], orientation["roll"]]
    predict_command(clf, angle)
