#  multiply all numbers up until the number itself
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(f'factorial is', factorial(7))
