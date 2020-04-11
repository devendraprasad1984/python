"""
START
Find the maximal sum of any double slice.
Programming language:
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

int solution(int A[], int N);

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""
def solution2(A):
    A_len = len(A)
    # Method: http://en.wikipedia.org/wiki/Maximum_subarray_problem
    max_ending_here = [0] * A_len
    max_ending_here_temp = 0
    for index in range(1, A_len - 2):
        max_ending_here_temp = max(0, A[index] + max_ending_here_temp)
        max_ending_here[index] = max_ending_here_temp
    max_beginning_here = [0] * A_len
    max_beginning_here_temp = 0
    for index in range(A_len - 2, 1, -1):
        max_beginning_here_temp = max(0, A[index] + max_beginning_here_temp)
        max_beginning_here[index] = max_beginning_here_temp
    max_double_slice = 0
    for index in range(0, A_len - 2):
        max_double_slice = max(max_double_slice,max_ending_here[index] + max_beginning_here[index + 2])
    return max_double_slice

# similar to max slice problem, only diff is we formed tripplet here
import random

def solution(A):
    N = len(A)
    A1 = [0]*N
    A2 = [0]*N
    maxCurrent = 0
    maxTotal = 0
    for i in range(1,N-1): A1[i] = maxCurrent = max( 0, maxCurrent + A[i] )
    maxCurrent = 0
    for i in range(N-2,0,-1): A2[i] = maxCurrent = max( 0, maxCurrent + A[i] )
    print(A1,A2)
    for i in range(1,N-1): maxTotal = max( maxTotal, A1[i-1] + A2[i+1] )
    return maxTotal

arr = [round(random.random()*1000) for i in range(50000)]
arr=[]
arr=[3,2,6,-1,4,5,-1,2]
print(solution(arr))
