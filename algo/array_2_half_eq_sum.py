"""
# Python3 program to split an array into Two
# equal sum subarrays

# Returns split point. If not possible, then
# return -1.
Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible

"""

def findSplitSumPoint(arr):
    n = len(arr)
    leftsum=0
    for i in range(n):
        leftsum+=arr[i]
        rightsum=0
        for j in range(i+1,n):
            rightsum+=arr[j]
        #splitIndex where both sums are equal
        if leftsum==rightsum:
            print(arr, " of which ","left sum is ",arr[0:i+1],str(leftsum),"and right sum is",arr[j-1:n],str(rightsum))
            return i+1
    print(arr,"split not possible")

# def print2parts(arr,n):
#     splitPos=findSplitSumPoint(arr,n)
#     if splitPos==-1 or splitPos==n:
#         print("split not possible")
#         return
#     for i in range(n):
#         if splitPos==i:
#             print("")
#         print(str(arr[i])+" ",end="")

arr = [1 , 2 , 3 , 4 , 5 , 5]
# print2parts(arr, n)
findSplitSumPoint(arr)
arr = [4, 1, 2, 3 ]
findSplitSumPoint(arr)
arr = [4, 3, 2, 1 ]
findSplitSumPoint(arr)
