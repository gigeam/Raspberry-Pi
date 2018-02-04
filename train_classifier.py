import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from sklearn.externals import joblib
import pandas as pd

n_neighbors = 25

# load the data_frame created using sense hat
df_source = pd.read_csv("angle_info.csv")
# use only a quarter of data
df = df_source.sample(frac=0.80, replace=False)
pitch = np.array(df["pitch"]).reshape(len(df["pitch"]), 1)
roll = np.array(df["roll"]).reshape(len(df["roll"]), 1)
# code the commands (i.e. replace the strings with a number code)
df["command"] = df["command"].replace("stop", 0)
df["command"] = df["command"].replace("forward", 1)
df["command"] = df["command"].replace("backward", 2)
df["command"] = df["command"].replace("left", 3)
df["command"] = df["command"].replace("right", 4)
y = np.array(df["command"])
X = np.concatenate((pitch, roll), axis=1)
print("data dimensions: ", X.shape, y.shape)

# step size in the mesh
h = .3  

# Create color maps [red, green, blue, yellow]
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#FDFD06'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#F0E94A'])

# 'uniform' : all points in each neighborhood are weighted equally.
# 'distance' : weight points by the inverse of their distance.
for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    """
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("5-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights))
    # y label
    plt.ylabel("Roll Angle")
    # x label
    plt.xlabel("Pitch Angle")
    """
    # save classifier
    joblib.dump(clf, 'knn_' + weights + '.pkl')

plt.show()

