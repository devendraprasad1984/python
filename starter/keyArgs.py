# Any keyword arguments you pass into this function will be placed into a dictionary named kwargs.
# You can examine the keys of this dictionary at run-time, like this:

def my_function(**kwargs):
    print(kwargs)


my_function(a=12, b="abc")


# There are two ways to assign argument values to function parameters, both are used.
# By Position. Positional arguments do not have keywords and are assigned first.
# By Keyword. Keyword arguments have keywords and are assigned second, after positional arguments.

def foo(*positional, **keywords):
    print("Positional: ", positional)
    print("Keywords: ", keywords)


foo('one', 'two', 'three')
foo(a='one', b='two', c='three')
foo('one', 'two', c='three', d='four')


def func(a='a', b='b', c='c', **kwargs):
    print('a:%s, b:%s, c:%s' % (a, b, c))


func()
func(**{'a': 'z', 'b': 'q', 'c': 'v'})
