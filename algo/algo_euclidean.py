"""
The Euclidean algorithm is one of the oldest numerical algorithms still to be in common
use. It solves the problem of computing the greatest common divisor (gcd) of two positive
integers.
lcm(a, b) = a*b / gcd(a,b)

Problem: Michael, Mark and Matthew collect coins of consecutive face values a, b and c
(each boy has only one kind of coins). The boys have to find the minimum amount of money
that each of them may spend by using only their own coins.
Solution: It is easy to note that we want to find the least common multiple of the three
integers, i.e. lcm(a, b, c). The problem can be generalized for the lcm of exactly n integers.

There is the following relation:
lcm(a1, a2,...,an) = lcm(a1, lcm(a2, a3,...,an))
We simply find the lcm n times, and each step works in logarithmic time
"""


def gcd_by_div(a, b):
    if a % b == 0:
        return b
    else:
        gcd_by_div(b, a % b)


def gcd_binary(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd_binary(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd_binary(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd_binary(a, b // 2, res)
    elif a > b:
        return gcd_binary(a - b, b, res)
    else:
        return gcd_binary(a, b - a, res)


def lcm(a, b):
    return int(a * b / gcd_binary(a, b,1))


# print(gcd_by_div(80,30))
a, b = 80, 30
print("gcd", a, b, gcd_binary(a, b, 1))
a, b = 10, 5
print("gcd", a, b, gcd_binary(a, b, 1))
a, b = 80, 30
print("lcm", a, b, lcm(a, b))



