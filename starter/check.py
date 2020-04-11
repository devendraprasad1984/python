def checkUsageOfListAndArray():
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]
    print("A0: ", A0)
    print("A1: ", A1)
    print("A2: ", A2)
    print("A3: ", A3)
    print("A4: ", A4)
    print("A5: ", A5)
    print("A6: ", A6)


def fn(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

fn(2)
fn(3, [3, 2, 1])
fn(3)  # l array will be stored in sessions memory as the variable is happening by reference here

checkUsageOfListAndArray()

# monkey patching - changing the behaviour of a function or overriding it
import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M"))
print(now, now.year, now.day, now.hour, now.month)
# datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)
print(datetime.datetime(2012, 12, 12).year)


print("args and kwargs")
# *arg - list, tuple, array
# *kwargs - key value pair, mapping object, like json


def f(*args, **kwargs): print(args, kwargs)

l = [1, 2, 3]
t = (4, 5, 6)
d = {'a': 7, 'b': 8, 'c': 9}

f()
f(1, 2, 3)
f(1, 2, 3, a=1, b=2)
f(*l, **d)
f(1, 2, *t, q="winning", **d)

# some class tets
class A(object):

    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):

    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):

    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
# b.go()
# c.go()
# d.go()
e.go()

# check profiling
def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

# import cProfile
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')
# cProfile.run('f3(lIn)')

def printDict(objDict):
    for key,value in objDict.items():
        print(str(key)+"->"+str(value))

print("a simple dictionary example")
states={"DEL":"DELHI","UP":"Uttar Pradesh"}
# print(str(states))
# loop over dictionary
printDict(states)

newState={"GO":"Goa"}
states.update(newState)
printDict(states)

# delete an object from dict
del states["GO"]
printDict(states)


a=b=range(5)
print(list(zip(a,b)))
print(tuple(zip(a,b)))
objDict=dict(zip(a,b))
print(str(objDict))
printDict(objDict)

# check anagrams
def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)

print(anagram("god","dog"))
print(anagram("aa","bb"))

# count frequency of each letter

count={}
for ltr in "djashdkasduueskaslas":
    if ltr in count:
        count[ltr]+=1
    else:
        count[ltr]=1
print(str(count))


# list comprehensions
lst=[1,2,3,4,5,6]
sqr=[i*i for i in lst]
sqr1={(i,i*i) for i in lst}
print(sqr,sqr1)


print("fib seq")
a,b=0,1
for i in range(1,10):
    print(a)
    a,b=b,a+b

print("fib by use of generators")
def fib(num):
    a,b=0,1
    for i in range(1,num):
        yield a
        a,b=b,a+b

# print("generators by next() keyword")
# x=fib(10)
# print(str(x.next()))

for i in fib(10):
    print(i)


#fixxbuzz
for i in range(101):
    if i%5==0 and i%3==0:
        print("FizzBuzz: "+str(i))
    # elif i%3==0:
    #     print("fizz: "+str(i))
    # elif i%5==0:
    #     print("buzz: "+str(i))
    # else:
    #     print("number is: "+str(i))



