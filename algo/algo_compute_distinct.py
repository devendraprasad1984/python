"""
Compute number of distinct values in an array.
Programming language:  Spoken language:
def solution(A)
that, given an array A consisting of N integers, returns the number of distinct values in array A.
For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# best
def solution2(A):
    num_distinct = len(list(set(A)))
    return num_distinct

# average
def solution(A):
    if len(A) == 0:
        distinct = 0
    else:
        distinct = 1
        A.sort()
        for index in range(1, len(A)):
            if A[index] == A[index - 1]:
                # The same element as the previous one
                continue
            else:
                distinct += 1
    return distinct


arr = [2, 1, 1, 2, 3, 1]
arr=[i for i in range(10000000)]
print("sol2: distinct value count", solution2(arr))
print("sol: distinct value count", solution(arr))
