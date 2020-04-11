print("Codility Sample test")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(nums):
    if not nums:
        return 1
    for i, v in enumerate(nums):
        if v > len(nums):
            nums[i] = -1
        elif v <= 0:
            nums[i] = -1
        else:
            while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
                # print (i, nums[i]-1, nums[i], nums[nums[i]-1])
                v = nums[i]
                nums[i] = nums[v - 1]
                nums[v - 1] = v
            if nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = -1
    for i, v in enumerate(nums):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


def first_missing_method1(nums):
    cnt = {}
    for x in nums:
        cnt[x] = 1
    print("object", cnt)
    fnd = 1
    for i in range(len(nums)):
        print("trying to find in dictionary object", fnd, cnt.get(fnd, 0))
        if cnt.get(fnd, 0) == 0:
            return fnd
        fnd += 1
    return fnd

# Pigeonhole principle
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


A = [2, 900, 999, 1000]
A = [-1, -3]
A = [1, 2, 3]
A = [3, 6, 4, 1, 2]
A = [1, 3, 6, 4, 1, 2]
# res = first_missing_method1(A)
# print("LOOP: smallest positive number which not in", A, "is", res)
res = find_missing_method2(A)
print("SET: smallest positive number which not in\n", A, "is\n", res)

# print(first_missing_positive(A))
