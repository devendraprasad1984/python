def fib(n):  # write Fibonacci series up to n
    if (n <= 0):
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# runtime is O(2powerN)
def allFib():
    for i in range(5):
        print(fib(i))


# memoization / caching - runtime is linear as we do constant work N times
def fib_memo(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def allFib_memo():
    memo = [0, 1]
    for i in range(4):
        print(i, memo, fib_memo(i, memo))


allFib_memo()
