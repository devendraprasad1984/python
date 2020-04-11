"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:
P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:
def solution(A)
that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].

Ans: The variable of head stores the sum of the heading part of the tape. And the variable of tail stores the sum of tailing part. Then, we move the index from 2nd position to the last 2nd position. Every time we move the index, we adjust both head and tail, compute and compare the difference.
"""
def solution(A):
    if A==[] or len(A)==1:
        return -1
    head=A[0]
    tail=sum(A[1:])
    min_diff=abs(head-tail)
    for i in range(1,len(A)-1):
        head+=A[i]
        tail-=A[i]
        if(abs(head-tail)<min_diff):
            min_diff=abs(head-tail)
    return min_diff

A=[3,5,2,4,3,6]
print(solution(A))
