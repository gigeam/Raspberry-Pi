print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import pandas as pd

n_neighbors = 20

# import some data to play with
iris = datasets.load_iris()

# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target

print(X.shape)
print(y.shape)

# load the data_frame created using sense hat
df_source = pd.read_csv("angles.csv")
df = df_source.sample(frac=0.2, replace=False)
pitch = np.array(df["pitch"]).reshape(len(df["pitch"]), 1)
roll = np.array(df["roll"]).reshape(len(df["roll"]), 1)
# code the commands (i.e. replace the strings with a number code)
df["command"] = df["command"].replace("stop", 0)
df["command"] = df["command"].replace("forward", 1)
df["command"] = df["command"].replace("backward", 2)
df["command"] = df["command"].replace("left", 3)
df["command"] = df["command"].replace("right", 4)
label = np.array(df["command"])
print(label)


X_t = np.concatenate((pitch, roll), axis=1)
print(X_t.shape)

X = X_t
y = label


h = .3  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

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
    # plt.pcolormesh(xx, yy, Z)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
    # plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.show()
