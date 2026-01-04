import pandas as pd

data=[10,20,30,40,50]

s=pd.Series(data,index=['a','b','c','d','e'])

print(s.sum())
print(s.mean())
print(s.min())
print(s.max())