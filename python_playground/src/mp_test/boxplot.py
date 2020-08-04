import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize =(10, 6.18))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0)

colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# changing color and line width of whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#8B008B',
                linewidth=1.5,
                linestyle=":")

# changing color and line width of caps
for cap in bp['caps']:
    cap.set(color='#8B008B', linewidth=5)

# changing color and line width of medians
for median in bp['medians']:
    median.set(color='red', linewidth=3)

# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker='D', color='#e7298a', alpha=0.5)

# x-axis labels
ax.set_yticklabels(['data_1', 'data_2', 'data_3', 'data_4'])

# Adding title
plt.title("Customized box plot")

# Removing top axes and right axes ticks
# ax.get_xaxis().tick_bottom()
# ax.get_yaxis().tick_left()

# show plot
plt.show()