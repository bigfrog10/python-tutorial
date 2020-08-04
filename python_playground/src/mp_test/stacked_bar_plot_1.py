import numpy as np
import matplotlib.pyplot as plt


countries = ['USA', 'GB', 'China', 'Russia', 'Germany']
bronzes = np.array([38, 17, 26, 19, 15])
silvers = np.array([37, 23, 18, 18, 10])
golds = np.array([46, 27, 26, 19, 17])

total = bronzes + silvers + golds
proportion_bronzes = bronzes / total * 100
proportion_silvers = silvers / total * 100
proportion_golds = golds / total * 100

plt.bar(countries, proportion_golds, width=0.8, label='golds', color='gold', bottom=proportion_bronzes+proportion_silvers)
plt.bar(countries, proportion_silvers, width=0.8, label='silvers', color='silver', bottom=proportion_bronzes)
plt.bar(countries, proportion_bronzes, width=0.8, label='bronzes', color='#CD853F')

plt.ylabel("Medals")
plt.xlabel("Countries")
plt.title("2012 Olympics Top Scorers' Medals by Proportion")
plt.ylim=1.0

# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()