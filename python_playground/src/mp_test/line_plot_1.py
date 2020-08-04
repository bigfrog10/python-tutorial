import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.2)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, **{'marker': 'x'})
plt.axhline(y=0, color='r', linestyle='-')

plt.show()