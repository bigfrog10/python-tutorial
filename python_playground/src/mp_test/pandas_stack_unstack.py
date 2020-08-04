# http://www.datasciencemadesimple.com/reshape-using-stack-unstack-function-pandas-python/
import pandas as pd
import numpy as np


header = pd.MultiIndex.from_product([['Semester1','Semester2'],['Maths','Science']])
d = ([[12, 45, 67, 56], [78, 89, 45, 67], [45, 67, 89, 90], [67, 44, 56, 55]])


df = pd.DataFrame(d, index=['Alisa', 'Bobby', 'Cathrine', 'Jack'], columns=header)
print(df)

stacked_df = df.stack()
print(stacked_df)

unstacked_df = stacked_df.unstack()
print(unstacked_df)

stacked_df_lvl=df.stack(level=0)
print(stacked_df_lvl)

