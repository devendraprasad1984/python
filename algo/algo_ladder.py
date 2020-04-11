"""
Count the number of different ways of climbing to the top of a ladder.
You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:
with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.
For example, given N = 4, you have five different ways of climbing, ascending by:
1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:
1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.
Write a function:
def solution(A, B)
that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].
For example, given L = 5 and:
    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.
Write an efficient algorithm for the following assumptions:
L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].
"""
def solution1(A, B):
    limit=len(A)
    rungs=[0]*limit
    fib=[0]*(limit+2)
    fib[1]=1
    for i in range(2,limit+2):
        fib[i]=fib[i-1]+fib[i-2]
    for i in range(limit):
        rungs[i]=fib[A[i]+1]%(1<<B[i])
    return rungs

def solution2(A, B):
    limit=len(A)
    rungs=[0]*limit
    fib=[0]*(limit+2)
    fib[1]=1
    B=[(1<<i)-1 for i in B] #pre compute B for optimisation
    for i in range(2,limit+2):
        fib[i]=fib[i-1]+fib[i-2]
    for i in range(limit):
        rungs[i]=fib[A[i]+1] & B[i]
    return rungs

def solution3(A, B):
    limit=len(A)
    rungs=[0]*limit
    fib=[0]*(limit+2)
    fib[1]=1
    modLimit=(1<<max(B))-1
    fib=getFibUsingLambda(limit+2)[1]
    # print("fib check",fib)
    # print("fib2",getFibUsingLambda(limit+2)[1])
    for i in range(limit):
        rungs[i]=fib[A[i]+1] & (1<<B[i])-1
    return rungs

def solution4(A,B):
    rungs=[]
    n=len(A)
    for i in range(n):
        num=(A[i]+1)%(2**B[i])
        rungs+=[num]
    return rungs

def getFibUsingLambda(x):
    n1=5**0.5
    n2=(1+n1)/2
    n3=(1-n1)/2
    fib = lambda i: int((n2**i - n3**i)/n1)
    fibArr=[fib(i) for i in range(x)]
    return fib(x),fibArr

A=[4,4,5,5,1]
B=[3,2,4,3,1]
# calc=(A[0]+1) % (2**B[0])
# print("modulo check",calc)
# print(solution1(A, B))
# print(solution2(A, B))
print(solution3(A, B))
# print(solution4(A, B))
# print(getFibUsingLambda(10))

