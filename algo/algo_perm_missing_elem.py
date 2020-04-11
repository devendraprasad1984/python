"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
Write a function:
def solution(A)
that, given an array A, returns the value of the missing element.
For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


def solution(items):
    if isinstance(items, list) == False:
        return 1
    elif items == []:
        return 1
    elif len(items) == 1:
        return items[0] + 1

    limit = max(items)
    sorted_item = sorted(items)
    num = 1
    # arr1=[i for i in range(0, limit)]
    for i in range(0, limit):
        if (i + 1) >= limit or i > len(items): break
        if sorted_item[i + 1] - sorted_item[i] > 1:
            num = sorted_item[i + 1] - 1
            break
    return num


def solution2(A):
    if isinstance(A, list) == False:
        return -1
    elif len(A) == 0:
        return -1
    elif len(A) == 1:
        return len(A) + 1

    n = len(A);
    totalSum = int(((n + 2) * (n + 1)) / 2)
    # totalSum = sum(A)
    for i in range(0, n):
        totalSum -= A[i]
    return len(A) + 1 if totalSum == 0 else totalSum
    # return abs(totalSum)


def solution3(A):
    if isinstance(A, list) == False:
        return 1
    elif A == []:
        return 1
    elif len(A) == 1:
        return A[0] + 1

    missing = A[0]
    sorted_array = sorted(A)
    for i in range(0, len(sorted_array)):
        if sorted_array[i] == missing:
            missing = sorted_array[i] + 1
    return missing


def solution4(A):
    sum = sum1 = 0
    for i in range(0, len(A)):
        sum += int(i + 1)
        sum1 += int(A[i])
    sum += int(i + 1)
    return int(sum - sum1)


arr = [i for i in range(1, 100000 + 1) if i != 1]
arr = [2, 3, 1, 5]
# arr = [1]
arr = [9, 11]
# arr = [99998, 100000]
# arr = [1041]
# print("missing num is", solution(arr))
print("missing num is", solution2(arr))
# print("missing num is", solution3(arr))
