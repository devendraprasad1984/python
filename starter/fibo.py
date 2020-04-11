# Fibonacci numbers module

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b  # double/multi assignment


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def getFib(x):
    # this is math rules for getting large fib nums
    n1=5**0.5
    n2=(1+n1)/2
    n3=(1-n1)/2
    fib = lambda x: int((n2**x - n3**x)/n1)
    fibRange=[fib(i) for i in range(x)]
    return fibRange

print(getFib(10))