def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


y = yrange(10)
print("1 Value: " + str(y.__next__()))
print("2 Value: " + str(y.__next__()))
print("3 Value: " + str(y.__next__()))
print("4 Value: " + str(y.__next__()))
print("5 Value: " + str(y.__next__()))


print([x*2 for x in range(10)])	
print({(x,x*2) for x in range(10)})	
print([(x,x*2) for x in range(10)])


# generator expressions (syntactic sweetness, class based geneators, yielding and most shorter is generator expressions)
iterator = ('Hello' for i in range(3))
for i in iterator:
    print("iterator value", i)
# for i in range(3):
#     print(next(iterator))

even_squares = lambda n: (x * x for x in range(n) if x % 2 == 0) #lambda function expressions
for i in even_squares(20):
    print("even squares",i)

#in line generator expressions
for i in (lambda n: (x * x for x in range(n) if x % 2 == 0))(10):
    print("even squares inline",i)




