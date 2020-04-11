"""
Determine whether a given string of parentheses (multiple types) is properly nested.
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.
Write a function:
def solution(S)
that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""


def solution(S):
    if len(S) % 2 == 1:   return 0
    nested_properly = 0
    matched = {'}': '{', ']': '[', ')': '('}
    to_push = ['[', '{', '(']
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


def solution2(S):
    if len(S) % 2 == 1:   return 0
    matched = {"]": "[", "}": "{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


S=[]
S = "([)()]"
S = "{[()()]}"
print(solution(S))
