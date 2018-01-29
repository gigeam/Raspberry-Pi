from sklearn.externals import joblib
import numpy as np


# predict command using loaded classifier
def predict_command(knn_clf, input_angle):
    codes = {0: "stop", 1: "forward", 2: "backward", 3: "left", 4: "right"}
    command = knn_clf.predict(np.array(input_angle).reshape(1, 2))[0]
    print("command: ", codes[command])
    return command


if __name__ == "__main__":
    clf = joblib.load('knn_distance.pkl')
    # [orientation["pitch"], orientation["roll"]]
    angle = [360, 360]
    predict_command(clf, angle)
