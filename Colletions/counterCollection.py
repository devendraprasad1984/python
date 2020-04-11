from collections import Counter

lst = [1,2,3,4,1,2,6,7,3,8,1]
cntr=Counter(lst)
print(lst)
print(cntr) #elements and occurances

print(list(cntr.elements())) #list back from counter object

print(list(cntr.most_common())) #return tuple

cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)

