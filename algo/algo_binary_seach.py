
def binarySearch(A,x):
    n=len(A)
    beg=0
    end=n-1
    res=-1
    while beg<=end:
        mid=int((beg+end)/2)
        if A[mid]==x: break
        if A[mid]>x: end=mid-1
        else: beg=mid+1
    res=mid
    return res

from random import random
n=100
x=58
A=[int(random()*n) for i in range(n)]
A=sorted(A)
# A=[i for i in range(n)]
print("trying to search ",x,"n",A)
print("found at position in array",binarySearch(A,x))

