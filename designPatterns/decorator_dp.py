#its a recursive composition or js function callbacks
# In general, decorators are ideal for extending the behavior of functions that we don't want to modify
# https://wiki.python.org/moin/

from functools import wraps #just for debugging as in big prog, you wont come to know where the call has originated from, similar to callback hell

def decorate_p_old(func):
    def func_wrapper(name):
        return "<p>"+func(name)+"</p>"
    return func_wrapper
"""A much better approach would be to make our decorator useful for functions and methods alike. This can be done by putting args and *kwargs as parameters for the wrapper, then it can accept any arbitrary number of arguments and keyword arguments."""
def decorate_p(func):
    def func_wrapper(*args,**kwargs):
        return "<p>"+func(*args,**kwargs)+"</p>"
    return func_wrapper
def decorate_div(func):
    def func_wrapper(name):
        return "<div>"+func(name)+"</div>"
    return func_wrapper
def decorate_strong(func):
    def func_wrapper(name):
        return "<strong>"+func(name)+"</strong>"
    return func_wrapper

# Passing arguments to decorators
def tags(tagname):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(*args,**kwargs):
            return "<{0}>{1}</{0}>".format(tagname,func(*args,**kwargs))
        return func_wrapper
    return tags_decorator

@decorate_div
@decorate_strong
@decorate_p
def get_wrapped_text(name):
    return "hello there - "+name

# without decoation
my_get_text=decorate_div(decorate_strong(decorate_p(get_wrapped_text)))
print(my_get_text("Devendra Prasad"),get_wrapped_text.__name__,get_wrapped_text.__doc__,get_wrapped_text.__module__)
# with decoration
my_get_text=get_wrapped_text
print(my_get_text("wow with decoration"))

class Person(object):
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln

    @decorate_p
    def get_wrapped_fullName(self):
        return self.fn+" - "+self.ln+" - welcome!!!"

    @tags("div")
    @tags("strong")
    def get_wrapped_fullName_tagged(self):
        return self.fn+" - "+self.ln+" - welcome!!!"

dp_prod_obj=Person("DP","PROD")
print(dp_prod_obj.get_wrapped_fullName())
xobj=dp_prod_obj.get_wrapped_fullName_tagged
print(xobj(), xobj.__name__)





# decoratory
"""
decorator - contract between client and framework
attaches additional functionality to an object and runtime, flexible way to subclassing for extending functionality
its like wrapping a gift, putting in box and wrapping that box also. You want to add behavior or state to individual objects at run-time. Inheritance is not feasible because it is static and applies to an entire class. give client the extra config for it to specify what extra ability it wants. Note that this pattern allows responsibilities to be added to an object, not methods to an object's interface. The interface presented to the client must remain constant as successive layers are specified. Also note that the core object's identity has now been "hidden" inside of a decorator object. Trying to access the core object directly is now a problem. consider christmas tree that has base functionality (green beautiful display, fir etc) and decorators like its ornaments stars, lights etc are the one that give extra functionality to it. Adapter provides a different interface to its subject. Proxy provides the same interface. Decorator provides an enhanced interface. Adapter changes an object's interface, Decorator enhances an object's responsibilities. Decorator is thus more transparent to the client. As a consequence, Decorator supports recursive composition, which isn't possible with pure Adapters. Composite and Decorator have similar structure diagrams, reflecting the fact that both rely on recursive composition to organize an open-ended number of objects. A Decorator can be viewed as a degenerate Composite with only one component. However, a Decorator adds additional responsibilities - it isn't intended for object aggregation. Decorator is designed to let you add responsibilities to objects without subclassing. Composite's focus is not on embellishment but on representation. These intents are distinct but complementary. Consequently, Composite and Decorator are often used in concert. Decorator and Proxy have different purposes but similar structures. Both describe how to provide a level of indirection to another object, and the implementations keep a reference to the object to which they forward requests. Decorator lets you change the skin of an object. Strategy lets you change the guts.

"""

"""
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
"""

import abc

class Component(metaclass=abc.ABCMeta):
    #Define the interface for objects that can have responsibilities added to them dynamically
    @abc.abstractmethod
    def operation(self):
        pass

class Decorator(Component, metaclass=abc.ABCMeta):
    #maintain the component ref and define an interface that conforms to component's interface
    def __int__(self, component):
        self._component=component

    @abc.abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    """add responsibilty to component"""
    def operation(self):
        self._component.operation()
class ConcreteDecoratorB(Decorator):
    """add responsibilty to component"""
    def operation(self):
        self._component.operation()

class ConcreteComponent(Component):
    """define object to which additional responsibility can be added"""
    def operation(self):
        print("inside ConcreteComponent")

def main():
    concrete_component=ConcreteComponent()
    concrete_decorator_a=ConcreteDecoratorA(concrete_component)
    concrete_decorator_b=ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()

if __name__ == '__main__':
    main()
