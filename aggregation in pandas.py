import pandas as pd

data=[10,20,30,40,50]

s=pd.Series(data,index=['a','b','c','d','e'])

print("\n Sum of data : ",s.sum())
print("\n Mean of data : ",s.mean())
print("\n Min of data : ",s.min())
print("\n Max of data : ",s.max())