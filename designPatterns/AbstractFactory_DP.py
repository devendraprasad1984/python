"""
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
\abc1-1.2.0>python setup.py install
"""

from abc import ABC, ABCMeta, abstractmethod

class AbstractProductA(metaclass=ABCMeta):
    #declare an interface for a type of product object
    @abstractmethod
    def interface_a(self):
        pass
class ConcreteProductA1(AbstractProductA):
    #define a product object to be create by the corresponding concerete factory, implement the abstractProduct interface
    def interface_a(self):
        return "ConcreteProductA1 - interface_a"
class ConcreteProductA2(AbstractProductA):
    #define a product object to be create by the corresponding concerete factory, implement the abstractProduct interface
    def interface_a(self):
        return "ConcreteProductA2 - interface_a"

class AbstractProductB(metaclass=ABCMeta):
    #declare an interface for a type of product object
    @abstractmethod
    def interface_b(self):
        pass
class ConcreteProductB1(AbstractProductB):
    #define a product object to be create by the corresponding concerete factory, implement the abstractProduct interface
    def interface_b(self):
        return "ConcreteProductB1 - interface_b"

class ConcreteProductB2(AbstractProductB):
    #define a product object to be create by the corresponding concrete factory, implement the abstractProduct interface
    def interface_b(self):
        return "ConcreteProductB2 - interface_b"



class AbstractFactory(metaclass=ABCMeta):
    # Declare an interface for operations that create abstract product    objects.
    @abstractmethod
    def create_product_a(self):
        pass
    @abstractmethod
    def create_product_b(self):
        pass

class ConcereteFactory1(AbstractFactory):
    # Implement the operations to create concrete product objects
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()
class ConcereteFactory2(AbstractFactory):
    # Implement the operations to create concrete product objects
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()

def main():
    for factory in (ConcereteFactory1(), ConcereteFactory2()):
        prod_a=factory.create_product_a()
        prod_b=factory.create_product_b()
        print(prod_a.interface_a(), prod_b.interface_b())

if __name__ == '__main__':
    main()