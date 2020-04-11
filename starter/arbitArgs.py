def manyArgs(*arg):
    # this is unpacking of arg list
    print("I was called with", len(arg), "arguments:", arg)
    for x in arg:
        print("arg value",x)


def print_tail(first, *tail):
    print(tail)


manyArgs(1)
manyArgs(1, 2, 3)

print_tail(1, 5, 2, "omega")


def make_dictionary(max_length=10, **entries):
    return dict([(key, entries[key]) for i, key in enumerate(entries.keys()) if i < max_length])


dict = make_dictionary(max_length=2, key1=5, key2=7, key3=9)
print(dict)
