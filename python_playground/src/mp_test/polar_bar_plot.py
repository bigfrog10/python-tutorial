import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


def polar_bar(labels, data):
    N = len(labels)
    ax = plt.axes([0.1, 0.1, 0.8, 0.8], polar=True)
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    width = 2 * np.pi / N

    clist = [(0, "red"), (0.125, "orange"), (0.25, "yellow"), (0.5, "green"),
             (0.6, "green"), (0.65, "blue"), (0.7, "darkblue"), (1, "purple")]
    rvb = mcolors.LinearSegmentedColormap.from_list("", clist)
    x = np.arange(N).astype(float)
    bars = plt.bar(theta, data, width=width, bottom=0.0, color=rvb(x / N), alpha=0.5)

    # for r,bar in zip(radii, bars):
    #     bar.set_facecolor(plt.cm.jet(r/10.))
    #     bar.set_alpha(0.5)

    ax.set_xticklabels(labels)
    ax.set_yticks(ax.get_yticks()[::3])
    # ax.set_yticklabels(labels1)
    # plt.tight_layout()
    plt.show()


labels = ['cat', 'dog', 'hand', 'eraser', 'frog', 'red', 'cow', 'white']
data = 1 + np.random.rand(len(labels))

polar_bar(labels, data)
