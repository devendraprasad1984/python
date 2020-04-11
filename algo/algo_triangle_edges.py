"""
Determine whether a triangle can be built from a given set of edges.
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.
Write a function:
def solution(A)
that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647]
"""


# follow basic tringle rules
# average
def solution2(A):
    sarr = sorted(A)
    count = 0;
    n = len(sarr);
    p = sarr[0];
    q = sarr[2]
    for i in range(0, n - 2):
        r = i + 2  # 3rd leg of triangle
        for j in range(i + 1, n):
            # Find the rightmost element which is smaller than the sum of two fixed elements
            while r < n and sarr[i] + sarr[j] > sarr[r]:
                r += 1
            count += (r - j - 1)
    return 1 if count > 0 else 0

# best
def solution(A):
    A_len = len(A)
    if A_len < 3: return 0
    A.sort()
    for index in range(0, A_len - 2):
        if A[index] + A[index + 1] > A[index + 2]:
            return 1
    return 0


arr = [10, 50, 5, 1]
arr = sorted([10, 2, 5, 1, 8, 20])
print(arr, "has tripplet for traingle is", solution(arr))
