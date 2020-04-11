"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:
def solution(A)
that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.
Write an efficient algorithm for the following assumptions:
N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

# worst time complexity O(nlogn)
def solution(A):
    new_arr = []
    left_unpaired=0
    for i in range(0, len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i]==A[j]:
                new_arr.append((i,j,A[i]))
                A[i]=A[j]=0
                break
        print(i,"th--->",A)
        left_unpaired=[k for k in A if k!=0]
    return new_arr,left_unpaired

# optimal design very fast and accurate with biggest of arrays
def getOddOccurrence_dp(arr):
    res = 0
    for element in arr:
        res = res ^ element # XOR with the result
    return res


arr = [9, 3, 9, 3, 9, 7, 9]
print("Array", arr)
new_array_of_off_left,left_unpaired=solution(arr)
print("pair of values found from array",new_array_of_off_left)
print("odd left without pair",left_unpaired[0])
print("using XOR odd left without pair", getOddOccurrence_dp(arr))
# print(arr.index(9,2))

