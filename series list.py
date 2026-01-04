import pandas as pd

#series - one dim array
data = [10,20,30,40,50]


s=pd.Series(data,index=['a','b','c','d','e'])  # for provoiding indexes
print(data)
print(s)