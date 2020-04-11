"""
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
A non-empty array A consisting of N integers is given.
The leader of this array is the value that occurs in more than half of the elements of A.
An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:
0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.
Write a function:
def solution(A)
that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""
from collections import Counter


def solution2(A):
    S = 0
    most_freq_elem = max(map(lambda val: (A.count(val), val), set(A)))
    print(most_freq_elem)
    most_freq_elem = max(set(A), key=A.count)
    print(most_freq_elem)
    most_freq_elem = Counter(A).most_common(1)[0]
    print("most common", most_freq_elem)
    return S


def solution1(A):
    counts = {}
    for i in A:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    S = max(counts)
    return S


def solution(A):
    a_len = len(A)
    candidate = -1
    candidate_count = 0
    for i in range(a_len):
        if candidate_count == 0:
            candidate = A[i]
            candidate_count += 1
        else:
            if A[i] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    leader_count = len([n for n in A if n == candidate])
    print(candidate_count, candidate, leader_count)
    if leader_count<=a_len/2:
        return 0
    else:
        leader=candidate
    equi_leaders=0
    leader_count_so_far=0
    for i in range(a_len):
        if A[i]==leader:
            leader_count_so_far+=1
        if leader_count_so_far>(i+1)//2 and leader_count-leader_count_so_far>(a_len-i-1)//2:
            equi_leaders+=1
    return equi_leaders

def solution4(A):
    # write your code in Python 2.7
    size = len(A)
    cnt, cnt1, s, ans = 0, 0, 0, 0
    for i in A:
        if 0 == cnt:
            s = i
        if s == i:
            cnt += 1
        else:
            cnt -= 1
    cnt = A.count(s)
    if cnt > size // 2:
        for i in range(size):
            if A[i] == s:
                cnt1 += 1
            if cnt1 > (i + 1) // 2 and cnt - cnt1 > (size - 1 - i) // 2:
                ans += 1
    return ans

A = [4, 3, 4, 4, 4, 2]
print(A)
print(solution(A))
