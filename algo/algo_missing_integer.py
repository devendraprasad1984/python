"""
Find the smallest positive integer that does not occur in a given sequence.
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def find_missing_method2(items):
    # l = [1,2,3,5,7,8,12,14]
    sorted_item = sorted(items)
    m = range(1, 1 + max(sorted_item))
    num = 1
    for i in m:
        if i not in sorted_item: break
        num = i + 1
    # print("min num from set",num)
    return num

def solution(A):
    sorted_elements = sorted(A)
    minVal = 1
    for elem in sorted_elements:
        if (elem == minVal):
            minVal += 1
    return minVal


arr = [1, 3, 6, 4, 1, 2]
arr = [-1, -3]
arr = [1, 2, 3]
arr = [99999]
print("smallest postive missing in ", arr, solution(arr))
