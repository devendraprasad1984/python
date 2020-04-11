"""
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True
Explanation


Hence, the output is True.
"""

# l=list(map(int,input().split()))
l=list(map(int,"2 15".split()))
px="x**4 - x - 1"
x,k=int(l[0]),int(l[1])
px=px.replace("x",str(x))
p=eval(px)
# for i in range(k):
#     p+=x**i
    # print(x**i, end=" ")
print(True if p==k else False)

