data ={"name":"ramesh",
       "date":"15",
       "month":"january",
       "year":"2006",
       "address":"siligiri"
}
print(data)
data1= data.copy()
name = input("Enter Name : ")
dat = input("Enter date :")
mon = input("Enter Month :")

data1['name'] = name
data1['date'] = dat
data1['month'] = mon
print(data1)
#print(data["name"])

#data.update()