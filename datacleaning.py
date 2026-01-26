import pandas as pd

df = pd.DataFrame({'A':[1,None,3],'B':['x','y',None]})
print("\n The elements of data frame \n")
print(df)
print("\n Null elements \n")
print(df.isnull())
# df1= df.fillna({'A':0,'B':'random'})    #replace null values
# print(df1)

df2=df.dropna()  #deleting null values
print("\n The elements after removing null \n")
print(df2)

df3=pd.DataFrame({"name" : ['Nive','Raja','Jana','Nive'],
                 'age': [25,25,18,25]})

print("\nThe duplicated values \n",df3.duplicated()) 
print("\n The elements after removing duplicates \n")    #to show duplicated value as true or false
print(df3.drop_duplicates())  #to remove duplicated values

df3=df3.rename(columns={'name':'Full_name'})  #to rename a column name
df3['name']=df3['Full_name'].str.lower()  #to use string operations
print("\n The elements of data frame after lower string operation  \n")
print(df3)

df3['name']=df3['Full_name'].str.contains("Raja")  #filter contains
print("\n The elements of data frame after contains string operation  \n")
print(df3)

df3['name']=df3['Full_name'].str.replace("Raja","Rajan")  #replacing string

print("\n The elements of data frame after replace string operation  \n")
print(df3)




