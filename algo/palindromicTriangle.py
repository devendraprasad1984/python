"""
Sample Input

5
Sample Output

1
121
12321
1234321
123454321
"""
n=5
x=[]
for i in range(1,n+1):
    # print(str(float('1'*i)**2).rstrip('.0'))
    print(pow(((pow(10,i)-1)//9),2))
    x.append(str(float('1'*i)**2).rstrip('.0'))
print(x)
