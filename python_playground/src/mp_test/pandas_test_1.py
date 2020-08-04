# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
# import seaborn as sns
#
# iris = sns.load_dataset('iris')
# print(iris.head())
# print(iris.shape)

import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(iris.head())
print(iris.shape)
iris.boxplot()

iris1 = iris.groupby('species').mean()
print(iris1)


def my_func(grouped_df):
    return grouped_df.sum(axis=0) / grouped_df.shape[0]


iris2 = iris.groupby('species').apply(my_func)
print(iris2)