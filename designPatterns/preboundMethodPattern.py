# A powerful technique for offering callables at the top level of your module that share state through a common object.
# eg random module and its top level objects randrange(), randint(), choice() that share states
# eg traditional but problematic approach
#First, it is impossible to ever instantiate a second copy of this random number generator. If two threads each wanted their own generator to avoid needing to protect it with locks, then they would be out of luck.
"""
(Okay, not really; this is Python. Think of the possibilities! You could import the module, save a reference to it, remove it
from the sys.modules dictionary, and then import it again to get a second copy. Or you could manually instantiate a second module
object and copy all three names across. By “out of luck” I refer only to sane Pythonic approaches.)
"""
from datetime import datetime
_seed = datetime.now().microsecond % 255 + 1
def set_seed(value):
    global _seed
    _seed = value

def random():
    global _seed
    _seed, carry = divmod(_seed, 2)
    if carry:
        _seed ^= 0xb8
    return _seed


# sol
from datetime import datetime

class Random8(object):
    def __init__(self):
        self.set_seed(datetime.now().microsecond % 255 + 1)

    def set_seed(self, value):
        self.seed = value

    def random(self):
        self.seed, carry = divmod(self.seed, 2)
        if carry:
            self.seed ^= 0xb8
        return self.seed

_instance = Random8() #private object
random = _instance.random
set_seed = _instance.set_seed

# When exercising this pattern, please be responsible about the dangers of instantiating an object at import time
# This pattern is usually not appropriate for a class whose constructor creates files, reads a database configuration, opens sockets, or that in general will inflict side effects on the program importing them


"""
One final hint: it is almost always better to assign methods to global names explicitly. 
Even if there are a dozen methods, I recommend going ahead and writing a quick stack of a dozen assignment statements aligned 
at the left-hand column of your module that make visible the whole list of global names you are defining. 
The fact that Python is a dynamic language might tempt you to automate the series of assignments instead, using 
attribute introspection and a for loop. I advise against it. Python programmers believe that 
“Explicit is better than implicit” 
— and materializing the stack of names as real code will better support human readers, language servers, and even venerable old grep.
"""

