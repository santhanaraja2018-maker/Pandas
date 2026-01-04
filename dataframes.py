import pandas as pd

#data frame

data={
    "id" : [1,2,3,4],
    "name" : ['John','Raja','Jana','Nive'],
    "email" : ["john@gmail.com","Raja@gmail.com","Jana@gmail.com","Nive@gmail.com"],
    "age":[30,25,18,25]
}

print (data)
s=pd.DataFrame(data)
print(s)
