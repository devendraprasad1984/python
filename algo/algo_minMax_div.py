"""
Divide array A into K blocks and minimize the largest sum of any block.
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.
The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
The large sum is the maximal sum of any block.
For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:
[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.
Write a function:
def solution(K, M, A)
that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.
For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.
Write an efficient algorithm for the following assumptions:
N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].
"""


def blockNo(A, maxBlock):
    blockNum = 1
    preBlockSum = A[0]
    for e in A[1:]:
        if preBlockSum + e > maxBlock:
            blockNum += 1
            preBlockSum = e
        else:
            preBlockSum += e
    return blockNum


def solution1(k, m, A):
    lbound, ubound = max(A), sum(A)
    res = 0
    if k == 1: return lbound
    if k >= len(A): return ubound
    #     binary search result
    while lbound <= ubound:
        resMaxMid = (lbound + ubound) // 2
        blocksNeeded = blockNo(A, resMaxMid)
        if blocksNeeded <= k:
            ubound = resMaxMid - 1
            res = resMaxMid
        else:
            lbound = resMaxMid + 1
    return res

    # superset = [(A[:i]+A[i+s:],sum(A[:i]+A[i+s:])) for i in range(n) for s in range(n)]


def solution(k, m, A):
    maxVal = sum(A)
    for i in range(len(A)):
        arr = A[i:]
        if len(arr) >= k:
            # set1+=[arr]
            print(arr)
            min_sum = sum(arr)
            if min_sum < maxVal:
                maxVal = min_sum
    return maxVal


A = [2, 1, 5, 1, 2, 2, 2]
A=[3,5,4]
k, m = 2, 5
print("minimum large sum is: ", solution(k, m, A))
