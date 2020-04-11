# import difflib
# from difflib_data import *

# s1 = [ 1, 2, 3, 5, 6, 4 ]
# s2 = [ 2, 3, 5, 4, 6, 1 ]

# print 'Initial data:'
# print 's1 =', s1
# print 's2 =', s2
# print 's1 == s2:', s1==s2
# print


xDict = dict(a=2, b=2, c=3, d=4)
yDict = dict(b=2, c=3, d=4)
xDict, yDict=zip(xDict.iteritems(), yDict.iteritems())
# unmatched_item = set(xDict.items()) ^ set(yDict.items()) #difference
unmatched_item = set(xDict.items()) - set(yDict.items())  # difference
print("UnMatched Items: " + str(unmatched_item))
matched_item = set(xDict.items()) & set(yDict.items())  # common
print("Matched Items: " + str(matched_item))
print("Loop over matched items and print elements")
for el in matched_item:
    print(el)

print("comparing sequences / tuple")
obj1 = (1, 2, 3)
obj2 = (2, 3, 4)
if (obj1 == obj2):
    print("equal")
else:
    print("not equal")

print("comparing lists")
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
if (obj1 == obj2):
    print("equal")
else:
    print("not equal")
