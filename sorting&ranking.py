import pandas as pd

df=pd.DataFrame({"name" : ['Nive','Raja','Jana','Nive'],
                 'age': [26,25,18,24]})
df1=df.sort_values(by='age')  #sort by values using age
df2=df.sort_index()

print("\nSorted Data by age\n",df1)
print("\nSorted Data by index\n",df2)

df3=pd.DataFrame({"score" : [100,40,30,67,89,45]},index=['a','b','c','d','e','f'])
df3["asc_rank"]=df3["score"].rank()   #ranking by score
print("\nAscending Ranked Data\n",df3)

df3["desc_rank"]=df3["score"].rank(ascending = False)   #ranking by score
print("\nDescending Ranked Data\n",df3)


df4=pd.DataFrame({"dpt":['hr','fin','it','hr','fin'],"sal" : [10040,3067,8945,3456,7565]},index=['a','b','c','d','e'])
print("\nGrouped by department and sum of salary Data\n",df4.groupby('dpt')['sal'].sum().reset_index(name='total_sum'))     # groupping by dpt and salary with operation sum

print("\nGrouped by department and Agg of salary Data\n",df4.groupby('dpt')['sal'].agg(['mean','min','max','count']).reset_index())  # groupping by dpt and salary with operation  all the agg as list