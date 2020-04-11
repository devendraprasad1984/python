"""

Dominator
START
Find an index of an array such that its value occurs at more than half of indices in the array.
Programming language:  Spoken language:
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""


def solution(A):
    # dom_elem= max(set(A), key=A.count)
    dom_elem = max(map(lambda val: (A.count(val), val), set(A)))
    if dom_elem[0] <= len(A) // 2:
        return -1
    else:
        # print(list(reversed(A)))
        elm_index=len(A)-1-list(reversed(A)).index(dom_elem[1])
        return elm_index


def solution2(A):
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1
    for index in range(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    if len([number for number in A if number == candidate]) <= A_len // 2:
        return -1
    else:
        return candidate_index


A = [1, 1, 1, 1, 2, 3, 4]
A = [1, 2, 3, 4, 5]
A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))
