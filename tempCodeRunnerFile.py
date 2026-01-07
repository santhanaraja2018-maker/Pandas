print(df[df['age']>20]) #here it prints all records where age >30

# print(df[df['name'].isin(['Raja'])]) #here it filters string value / name is in list form so here also we pass it as list

# print (df[df['age'].between(18,25)])  #here it filters age using between18 amd 25 (includes first and last value)

# print(df.query("age>18")) #here it filters age using query >18


# print(df.age)
# print(df.email)