"""
Python | Inserting item in sorted list maintaining order

"""
test_list = [1, 2, 3, 6, 7]
print ("The original list is : " + str(test_list))
k=5
#insert in a sorted list using naive method
for i in range(len(test_list)):
    if test_list[i]>k:
        index=i
        break
res=test_list[:index]+[k]+test_list[index:]
print ("The modified list is : " + str(res))



import bisect
test_list = [1, 2, 3, 6, 7]
print ("The original list is : " + str(test_list))
bisect.insort(test_list, 5)
bisect.insort(test_list, 8)
print ("The list after insertion is : " +  str(test_list))

