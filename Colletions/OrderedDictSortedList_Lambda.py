from collections import OrderedDict

dct={}

dct["z"]=1
dct["o"]=2
dct["x"]=3
dct["d"]=4
dct["m"]=5

for x in dct:
    print("items are",x,dct[x])

for x in dct.items():
    print(x)

lis = [{ "name" : "Nandini", "age" : 20},
       { "name" : "Manjeet", "age" : 18 },
       { "name" : "Nikhil" , "age" : 19 }]
print("printing list sorting by age",sorted(lis,key=lambda i:i["age"],reverse=True))
print("printing list sorting by name",sorted(lis,key=lambda i:i["name"]))
print("list of sorted items",sorted([10,8,5,3,42,2,9],key=lambda i:i))
