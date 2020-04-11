# simple yet powerful way for algo
def generateFactorial(n):
    factorial = 1
    for i in range (1, n + 1):
        factorial *= i
    return factorial

# n choose k algo
# recursive factorial,  and multiplicative
# best for subset related computational algo

def nck_recursive(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return nck_recursive(n - 1, k) + nck_recursive(n - 1, k - 1)


def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

# n!/(k!*(n-k)!)
def nck_factorial(n,k):
    return fact(n)/(fact(k)*fact(n-k))

def nck_multiplicative(n,k):
    res=1
    for i in range(1,k+1):
        res=res*(n-(k-i))/i
    return res


print("factorial5",generateFactorial(5))
print("factorial10",generateFactorial(10))
print("factorial15",generateFactorial(15))
print("factorial20",generateFactorial(20))
print("factorial25",generateFactorial(30))
print("factorial30",generateFactorial(40))


# choose n k programming methods, all these do the same thing
n = 30
k = 10
print("factortial",fact(n))
print("nck_multiplicative",nck_multiplicative(n, k))
print("nck_factorial",nck_factorial(n, k))
print("nck_recursive",nck_recursive(n, k))
