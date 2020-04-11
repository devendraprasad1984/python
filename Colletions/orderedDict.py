from collections import OrderedDict
from collections import Counter

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

for key, value in od.items():
    print(key, value)


list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
print("counter",cnt)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)




