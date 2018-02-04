import matplotlib.pyplot as plt
import pandas as pd

# load the data_frame created using sense hat
df = pd.read_csv("angle_info.csv")

# Create a figure
plt.figure(figsize=(20, 20))

# Create a scatter-plot of,
# pitch angle, in command stop, as the x axis
plt.scatter(df["pitch"][df["command"] == "stop"],
            # roll angle, in command stop, as the y axis
            df["roll"][df["command"] == "stop"],
            # the marker as
            marker="x",
            # the color i.e. red
            color="#FF0000",
            # the alpha
            alpha=0.7,
            # with size
            s=100,
            # labelled this
            label="stop")

# pitch angle, in command forward, as the x axis
plt.scatter(df["pitch"][df["command"] == "forward"],
            # roll angle, in command forward, as the y axis
            df["roll"][df["command"] == "forward"],
            # the marker as
            marker="^",
            # the color i.e. green
            color="#00FF00",
            # the alpha
            alpha=0.7,
            # with size
            s=100,
            # labelled this
            label="forward")

# pitch angle, in command backward, as the x axis
plt.scatter(df["pitch"][df["command"] == "backward"],
            # roll angle, in command backward, as the y axis
            df["roll"][df["command"] == "backward"],
            # the marker as
            marker="v",
            # the color i.e. blue
            color="#0000FF",
            # the alpha
            alpha=0.7,
            # with size
            s=100,
            # labelled this
            label="backward")

# pitch angle, in command left, as the x axis
plt.scatter(df["pitch"][df["command"] == "left"],
            # roll angle, in command left, as the y axis
            df["roll"][df["command"] == "left"],
            # the marker as
            marker="<",
            # the color i.e. yellow
            color="#F0E94A",
            # the alpha
            alpha=0.7,
            # with size
            s=100,
            # labelled this
            label="left")

# pitch angle, in command right, as the x axis
plt.scatter(df["pitch"][df["command"] == "right"],
            # roll angle, in command right, as the y axis
            df["roll"][df["command"] == "right"],
            # the marker as
            marker=">",
            # the color i.e. purple
            color="#810C9C",
            # the alpha
            alpha=0.7,
            # with size
            s=100,
            # labelled this
            label="right")

# Chart title
plt.title("Manually Annotated Commands")

# y label
plt.ylabel("Roll Angle")

# x label
plt.xlabel("Pitch Angle")

# and a legend
plt.legend(loc="center right")

# set the figure boundaries
plt.xlim([min(df["pitch"]), max(df["pitch"])])
plt.ylim([min(df["roll"]), max(df["roll"])])

plt.show()
