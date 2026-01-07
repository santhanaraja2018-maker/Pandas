import pandas as pd

df=pd.read_csv(r"C:\Users\SANTHANA RAJA S\Desktop\Git\Pandas\data.csv")

print(df)
print(df.head()) # it will give top 5 values

print(df.head(8)) # it will give top 8 values

print(df.tail(8)) # it will give bottom 8 values
print(df.tail()) # it will give bottom 5 values


print(df.info())  #it will give overview of datatypes,null values,memory
print(df.describe()) #it will give all the statistical data
