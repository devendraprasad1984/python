# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

print("input 2 numbers")
x=3 #input()
y=5 #input()
print("input numbers are",x,y)
arr=[[i for i in range(y)] for j in range(x)]
print("array is ",arr)
cnt=0
newVal=0
for i in arr:
    j=0
    for x in i:
        newVal=x*cnt
        # print(newVal)
        arr[cnt][j]=newVal
        j+=1
    cnt+=1
print(arr)