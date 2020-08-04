# library &amp; dataset
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Grouped violinplot
sns.violinplot(x="day", y="total_bill", hue="sex", data=df, palette="Pastel1")
plt.show()