"""
Determine whether a given string of parentheses (single type) is properly nested.
A string S consisting of N characters is called properly nested if:
S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.
Write a function:
def solution(S)
that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.\
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
"""


def solution2(S):
    if len(S) == 0:   return 0
    nested_properly = 0
    matched = {')': '('}
    to_push = ['(']
    heap = []
    for i in S:
        if i in to_push:
            heap.append(i)
        else:
            if len(heap) == 0:
                return 0
            elif matched[i] != heap.pop():
                return 0
    if len(heap) == 0:
        nested_properly = 1
    else:
        nested_properly = 0

    return nested_properly


def solution(S):
    parentheses = 0
    for element in S:
        if element == "(":
            parentheses += 1
        else:
            parentheses -= 1
            if parentheses < 0:
                return 0
    if parentheses == 0:
        return 1
    else:
        return 0


S = "(()"
S = "(()(())())"
print(solution(S))
