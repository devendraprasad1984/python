"""
In Python, there is something called name mangling, which means that there is a limited support for a valid use-case for class-private members basically to avoid name clashes of names with names defined by subclasses. Any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek, where classname is the current class name with leading underscore(s) stripped. As long as it occurs within the definition of the class, this mangling is done. This is helpful for letting subclasses override methods without breaking intraclass method calls.

"""

# Python code to illustrate how mangling works
class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)
    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

            # private copy of original geek() method
    __geek = geek

class MapSubclass(Map):

    # provides new signature for geek() but
    # does not break __init__()
    def geek(self, key, value):
        for i in zip(keys, values):
            self.list.append(i)

