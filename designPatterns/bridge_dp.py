"""
Decouple an abstraction from its implementation so that the two can vary
independently.
"""

import abc

class Abstraction:
    #Define the abstraction's interface. Maintain a reference to an object of type Implementor.
    def __init__(self,imp):
        self._imp=imp
    def operation(self):
        return self._imp.operation_imp()

class implementor(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes. This interface
    doesn't have to correspond exactly to Abstraction's interface; in
    fact the two interfaces can be quite different. Typically the
    Implementor interface provides only primitive operations, and
    Abstraction defines higher-level operations based on these
    primitives.
    """
    @abc.abstractmethod
    def operation_imp(self):
        pass

# Implement the Implementor interface and define its concrete implementation.
class ConcreteImplementorA(implementor):
    def operation_imp(self):
        print("inside ConcreteImplementorA operation_imp")
        return "x"
class ConcreteImplementorB(implementor):
    def operation_imp(self):
        print("inside ConcreteImplementorB operation_imp")
        return "y"


def main():
    for impl in (ConcreteImplementorA(), ConcreteImplementorB()):
        abstraction=Abstraction(impl)
        print(abstraction.operation())

if __name__ == '__main__':
    main()