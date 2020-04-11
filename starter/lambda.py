# function object
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)

ival = f(0)
print("The Sum by function object is: " + str(ival))
ival = f(45)
print("The Sum by function object is: " + str(ival))

# pass a small function as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

g = lambda x: x**2
print(g(8),g(9))
print(f(10),make_incrementor(10)(50))

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x%3 == 0, foo))
print(lambda x: x*2+10,foo)

print(map(lambda w: len(w), 'It is raining cats and dogs'.split()))
