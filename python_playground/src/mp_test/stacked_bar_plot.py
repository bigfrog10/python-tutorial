import numpy as np
import matplotlib.pyplot as plt

countries = ['USA', 'GB', 'China', 'Russia', 'Germany']
bronzes = np.array([38, 17, 26, 19, 15])
silvers = np.array([37, 23, 18, 18, 10])
golds = np.array([46, 27, 26, 19, 17])
ind = [x for x, _ in enumerate(countries)]

# plt.bar(ind, golds, width=0.8, label='golds', color='gold', bottom=silvers+bronzes)
# plt.bar(ind, silvers, width=0.8, label='silvers', color='silver', bottom=bronzes)
# plt.bar(ind, bronzes, width=0.8, label='bronzes', color='#CD853F')

plt.bar(countries, golds, width=0.8, label='golds', color='gold', bottom=silvers+bronzes)
plt.bar(countries, silvers, width=0.8, label='silvers', color='silver', bottom=bronzes)
plt.bar(countries, bronzes, width=0.8, label='bronzes', color='#CD853F')

# plt.xticks(ind, countries)
plt.ylabel("Medals")
plt.xlabel("Countries")
plt.legend(loc="upper right")
plt.title("2012 Olympics Top Scorers")

plt.show()