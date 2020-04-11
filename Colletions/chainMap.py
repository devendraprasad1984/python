"""simple chain map test"""

from collections import ChainMap

dict1={"a":1,"b":2}
dict2={"x":3,"y":4}

chmap=ChainMap(dict1,dict2)
dict2["zy"]=10 # objects are by reference
print(chmap,chmap.maps,chmap["a"])

dict3={}
dict3["1"]=20
dict3["2"]=20
dict3["3"]=20
dict3["4"]=20

newChainMap=chmap.new_child(dict3)
print("new chain map",newChainMap)

print("chain maps",chmap.maps)
print("keys",list(chmap.keys()))
print("values",list(chmap.values()))

for ch in chmap:
    print(ch,chmap[ch])
