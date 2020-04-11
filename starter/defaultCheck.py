# There is much more to it than you think. Consider the defaults to be static (=constant reference pointing to one object) and
#  stored somewhere in the definition; evaluated at method definition time; as part of the class, not the instance. 
#  As they are constant, they cannot depend on self.
# Here is an example. It is counterintuitive, but actually makes perfect sense:
def add(item, s=[]):
    s.append(item)
    print("Example1: the static list length is: " + str(len(s)))


add(1)
add(1)
add(1, [])
add(1)

# Because it works the same way as
default_s = []


def add1(item, s=default_s):
    s.append(item)
    print("Example2: the static list length is: " + str(len(s)))


add1(1)
add1(1)
add1(1, [])
add1(2)


def log(message=None):
    if message:
        print("LOG: {0}".format(message))


log("Print my message")
log()

# class Foo:
#     import types
#     def add2(self, item, s=Foo.defaultFactory):
#         if isinstance(s, types.FunctionType): s = s(self)
#         s.append(item)

#     def defaultFactory(self):
#         """ Can be overridden in a subclass, too!"""
#         return []

# foo=Foo()
# foo.add(1)
# foo.add(2)
# foo.add(1,[])
# foo.add(3)


# use of lambda default
import types


def add4(item, s=lambda self: []):
    if isinstance(s, types.FunctionType): s = s("example")
    s.append(item)


add4(1)
add4(2)
add4(3, [])
