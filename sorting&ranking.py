import pandas as pd

df=pd.DataFrame({"name" : ['Nive','Raja','Jana','Nive'],
                 'age': [26,25,18,24]})
df1=df.sort_values(by='age')  #sort by values using age
df2=df.sort_index()

print(df1)
print(df2)

df3=pd.DataFrame({"score" : [100,40,30,67,89,45]},index=['a','b','c','d','e','f'])
df3=df3["score"].rank()   #ranking by score
print(df3)



df4=pd.DataFrame({"dpt":['hr','fin','it','hr','fin'],"sal" : [10040,3067,8945,3456,7565]},index=['a','b','c','d','e'])
print(df4.groupby('dpt')['sal'].sum())     # groupping by dpt and salary with operation sum

print(df4.groupby('dpt')['sal'].agg(['mean','min','max','count']))  # groupping by dpt and salary with operation  all the agg as list