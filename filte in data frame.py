import pandas as pd

data={
    "id" : [1,2,3,4],
    "name" : ['John','Raja','Jana','Nive'],
    "email" : ["john@gmail.com","Raja@gmail.com","Jana@gmail.com","Nive@gmail.com"],
    "age":[30,25,18,25]
}

df=pd.DataFrame(data, index=['a','b','c','d'])
print(df.loc['b'])  #here we use loc to access data using lables

print(df.iloc[0])  #here we use iloc to access data using indexes
print(df.iloc[2,3]) #here we use iloc[2,3] to access data using indexes 2nd row 3rd index data

print(df[df['age']>20]) #here it prints all records where age >30

print(df[df['name'].isin(['Raja'])]) #here it filters string value / name is in list form so here also we pass it as list

print (df[df['age'].between(18,25)])  #here it filters age using between18 amd 25 (includes first and last value)

print(df.query("age>18")) #here it filters age using query >18


print(df.age)
print(df.email)