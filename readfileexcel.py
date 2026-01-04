import pandas as pd

df=pd.read_excel("sample.xlsx",sheet_name="Sheet1")

df1=df.head()
df1.to_csv("firstfive.csv",index=False) # saving some data as csv file

df2=df.tail()
df2.to_excel("lastfive.xlsx",index=False)

print(df)
print(df.head()) # it will give top 5 values

print(df.head(8)) # it will give top 8 values

print(df.tail(8)) # it will give bottom 8 values
print(df.tail()) # it will give bottom 5 values


print(df.info())  #it will give overview of datatypes,null values,memory
print(df.describe()) #it will give all the statistical data