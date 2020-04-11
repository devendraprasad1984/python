"""
Array of 0’s and 1’s. Move 0’s to left and 1’s to right side
https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
"""

# method1
cnt=0
arr=[1,0,1,0,1,1,1,0,1,0,0,0,1,0,1]
for i in range(len(arr)):
    if arr[i]==0:
        arr[cnt]=arr[i]
        cnt+=1
while cnt<len(arr):
    arr[cnt]=1
    cnt+=1

print("original array moved",arr)


# method2
arr=[1,0,1,0,1,1,1,0,1,0,0,0,1,0,1]
nArr=[-1 for x in arr]
ln=len(arr)
left=0
right=ln-1
print("original",arr)
for i in arr:
    if i==0:
        nArr[left]=i
        left+=1
    else:
        nArr[right]=i
        right-=1
print("after movement",nArr)

# method3
arr=[1,0,1,0,1,1,1,0,1,0,0,0,1,0,1]
cnt0,cnt1=0,0
for i in range(ln):
    if arr[i]==1:
        cnt1+=1
    else:
        cnt0+=1
print("count of 0/1",cnt0,cnt1)
for i in range(cnt0):
    arr[i]=0
for i in range(cnt1,ln):
    arr[i]=1
print("original array moved",arr)
