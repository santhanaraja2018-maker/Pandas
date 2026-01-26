import pandas as pd

data={
    "id" : [1,2,3,4],
    "name" : ['John','Raja','Jana','Nive'],
    "email" : ["john@gmail.com","Raja@gmail.com","Jana@gmail.com","Nive@gmail.com"],
    "age":[30,25,0,25]
}

df=pd.DataFrame(data, index=['a','b','c','d'])
print("\nData \n",df)
print("\n The value at declared index b \n ",df.loc['b'])  #here we use loc to access data using lables

print("\n The value at original index 0 \n ",df.iloc[0])  #here we use iloc to access data using indexes
print("\n The value at original index 2,3 in data frame: ",df.iloc[2,3]) #here we use iloc[2,3] to access data using indexes 2nd row 3rd index data

print("\n The value age = 0 \n ",df[df['age']==0]) #here it prints all records where age = 0
df.loc[df['age']==0, 'age'] = 20
print ("\n The value after changing age  0  to 20 \n ",df['age'])

print("\n The names in raja \n",df[df['name'].isin(['Raja'])]) #here it filters string value / name is in list form so here also we pass it as list

print ("\n The names between 18 to 25 \n ",df[df['age'].between(18,25)])  #here it filters age using between18 amd 25 (includes first and last value)

print("\n The age > 18 \n ",df.query("age>18")) #here it filters age using query >18


print("\n Ages  \n",df.age)
print("\n Email  \n",df.email)