import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 5)
plt.bar(x, x, 0.1,  label='linear')
plt.bar(x + 0.1, x**2, 0.1, label='quadratic')
plt.bar(x + 0.2, x**3, 0.1, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.title('simple plot')
plt.show()