"""

MaxSliceSum
START
Find a maximum sum of a compact subsequence of array elements.
Programming language:  Spoken language:
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
"""


def solution3(A):
    max_sum = 0
    n = len(A)
    # twoDArray=[[0]*n]*n
    # print(np.array(twoDArray))
    for i in range(n):
        new_sum = sum(A[i:i + 2])
        if max_sum < new_sum:
            max_sum = new_sum
    return max_sum


def solution2(A):
    A_len = len(A)  # The length of array A
    # Get the sum of maximum subarray, which ends this position
    # Method: http://en.wikipedia.org/wiki/Maximum_subarray_problem
    max_ending_here = [0] * A_len
    max_ending_here_temp = 0
    for index in range(1, A_len - 2):
        max_ending_here_temp = max(0, A[index] + max_ending_here_temp)
        max_ending_here[index] = max_ending_here_temp
    # Get the sum of maximum subarray, which begins this position
    # The same method. But we travel from the tail to the head
    max_beginning_here = [0] * A_len
    max_beginning_here_temp = 0
    for index in range(A_len - 2, 1, -1):
        max_beginning_here_temp = max(0, A[index] + max_beginning_here_temp)
        max_beginning_here[index] = max_beginning_here_temp
    # Connect two subarray for a double_slice. If the first subarray
    # ends at position i, the second subarray starts at position i+2.
    # Then we compare each double slice to get the one with the
    # greatest sum.
    max_double_slice = 0
    for index in range(0, A_len - 2):
        max_double_slice = max(max_double_slice,
                               max_ending_here[index] + max_beginning_here[index + 2])
    return max_double_slice

# best case complexity O(N)
def solution(A):
    max_ending_here = max_so_far = A[0]
    for i in A[1:]:
        max_ending_here=max(i, max_ending_here+i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

A=[-10]
A = [3, 2, -6, 4, 0]
print(A, "\n", solution(A))
