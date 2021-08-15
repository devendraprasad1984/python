import math

print("binary search with ologn complexity")
arr = []
start = 0
arr = [i for i in range(0, 1000)]  # prepare input
end = len(arr) - 1
target = 192


def binarySeach(arr, start, end):
    if start > end: return False
    mid = math.floor((start + end) / 2)
    if arr[mid] == target: return True
    if (arr[mid] > target):
        return binarySeach(arr, start, mid - 1)
    else:
        return binarySeach(arr, mid + 1, end)


found = binarySeach(arr, start, end)
print(f'found {target}', found)
