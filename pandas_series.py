# syntax pd.Series(data, index)
import pandas as pd

list1 = [10,20,40,60]

series_ex1 = pd.Series(list1)
print(series_ex1)

'''
o/p: 

0    10
1    20
2    40
3    60
dtype: int64
'''

#manually giving the index

a = ['a','b','c','d']
series_ex2 = pd.Series(list1,a)
print(series_ex2)

'''
o/p

a    10
b    20
c    40
d    60
dtype: int64
'''

