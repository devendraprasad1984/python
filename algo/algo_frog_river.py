"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.
For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
Write a function:
def solution(X, A)
that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
If the frog is never able to jump to the other side of the river, the function should return −1.
For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.
Write an efficient algorithm for the following assumptions:
N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""


def solution(X, A):
    earliest_position_int = -1
    matchOnce = False
    for i, v in enumerate(A):
        if v == X:
            earliest_position_int = i
    return earliest_position_int


# this is the most accurate one to this problem
def solution2(X, A):
    covered_time = [-1] * X  # Record the time, each position is covered
    uncovered = X  # Record the number of uncovered position
    for index in range(0, len(A)):
        if covered_time[A[index] - 1] != -1:
            continue
        else:
            covered_time[A[index] - 1] = index
            uncovered -= 1
            if uncovered == 0:
                return index
    return -1


def solution3(X, A):
    covered = 0
    covered_a = [-1] * X
    for i, v in enumerate(A):
        if v-1>len(covered_a)-1:
            continue
        elif covered_a[v - 1] == -1:
            covered_a[v - 1] = v
            covered += 1
            if covered == X:
                return i
    return -1


def solution1(X, A):
    distinctList = list(set(A))
    return -1 if A.index(X) <= -1 else A.index(X)


X = 2
arr = [i for i in range(100000 + 1)]
arr = []
arr = [1, 3, 1, 4, 2, 3, 5, 4]
arr = [2, 2, 2, 2, 2]
# print(arr)
print("earliest moment leaves are all \nin water that frog can cover \nto reach X point is"
      , solution3(X, arr))
