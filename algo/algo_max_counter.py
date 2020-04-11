"""
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
You are given N counters, initially set to 0, and you have two possible operations on them:
increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:
if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.
Write a function:
def solution(N, A)
that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.
Result array should be returned as an array of integers.
For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.
Write an efficient algorithm for the following assumptions:
N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


def solution(N, A):
    new_array = [0] * N
    max_counter = 0
    for i in range(len(A)):
        if A[i] == N + 1:
            max_counter = max(new_array)
            new_array = [max_counter] * len(new_array)
        elif 1 <= A[i] <= N:
            new_array[A[i] - 1] += 1
            if new_array[A[i] - 1] > max_counter:
                max_counter = new_array[A[i] - 1]
    return new_array


# lazy write method for best performance
def solution2(N, A):
    result = [0] * N  # The list to be returned
    max_counter = 0  # The used value in previous max_counter command
    current_max = 0  # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command - 1]:
                # lazy write
                result[command - 1] = max_counter
            result[command - 1] += 1
            if current_max < result[command - 1]:
                current_max = result[command - 1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0, N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous max_counter command
            result[index] = max_counter
    return result


arr = [3, 4, 4, 6, 1, 4, 4]
print("old array", arr)
print("new array", solution(5, arr))
