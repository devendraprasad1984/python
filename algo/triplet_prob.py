"""
2) Triplet problem.
Array = {2,3,7,6,8,9} and k=6.
{2,3,6} (2×3 = 6)
{3,2,6} (3×2 = 6)
"""

arr=[2,3,4,7,6,8,9,12]
arr.sort()
k=6
print(arr,k)

finalVals=[]
size=arr.__len__()
for i in range(0,size-1):
    a=arr[i]
    b=arr[i+1]
    if arr.__contains__(a*b): #and a*b==k:
        finalVals.append([a,b,a*b])
        finalVals.append([b,a,b*a])

print(finalVals)

def compareTriplets(a, b):
    alice=0
    bob=0
    for i,v in enumerate(a):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            continue
    return [alice, bob]
a = list(map(int, "5 6 7".rstrip().split()))
b = list(map(int, "3 6 10".rstrip().split()))
result = compareTriplets(a, b)
print(' '.join(map(str, result)))
