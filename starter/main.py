# Due to the global interpreter lock (GIL), Python is—by design—a single-threaded language

from starter import mdFunc, fibo, mdDs, mdPrint

print("Calling Func: ", mdFunc.ver)
mdFunc.runLoop()
print("Calling Print: ", mdPrint.ver)
mdPrint.printTest()
print("Calling simple data structure")
mdDs.makeList()
mdDs.makeSet()

# from fibo import fib, fib2
fibo.fib(10)
dVar = dir(fibo)
print(dVar)
print(__file__)
# unc.ver
mdFunc.runLoop()
print("Calling Print: ", mdPrint.ver)
mdPrint.printTest()
print("Calling simple data structure")
mdDs.makeList()
mdDs.makeSet()

# from fibo import fib, fib2n`
fibo.fib(10)
dVar = dir(fibo)
print(dVar)
print(__file__)

fn = lambda x: (x % 7) * 2
keys = [x for x in range(1, 100)]
print("keys: ", keys)
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
objDict = {k: v * 2 for (k, v) in dict1.items()}
print("dict loop: ", objDict)
objDict = {k: k * 2 for k in keys}
print("array list loop: ", objDict)

# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple
# input_data = input("input comma separated string\n")
# l = input_data.split(',')
# t = tuple(l)
# print(l, t)

print("some format check")
xTest = '{} len={}'.format(type('testcontent').__name__, len('testcontent'))
print(xTest)
xTest = '{}, len={}'.format('content length is ', len('testcontent'))
print(xTest)



