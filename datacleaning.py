import pandas as pd

df = pd.DataFrame({'A':[1,None,3],'B':['x','y',None]})
print(df)
print(df.isnull())
# df1= df.fillna({'A':0,'B':'random'})    #replace null values
# print(df1)

df2=df.dropna()  #deleting null values
print(df2)

df3=pd.DataFrame({"name" : ['Nive','Raja','Jana','Nive'],
                 'age': [25,25,18,25]})

print("The duplicated values : ",df3.duplicated())     #to show duplicated value as true or false
print(df3.drop_duplicates())  #to remove duplicated values

df3=df3.rename(columns={'name':'Full_name'})  #to rename a column name
df3['name']=df3['Full_name'].str.lower()  #to use string operations
df3['name']=df3['Full_name'].str.contains("Raja")  #filter contains


df3['name']=df3['Full_name'].str.replace("Raja","Rajan")  #replacing string


print(df3)




