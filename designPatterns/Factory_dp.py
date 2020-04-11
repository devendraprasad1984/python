"""
Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
"""

import abc


#Define the interface of objects the factory method creates.
class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass
# Implement the Product interface.
class ConcreteProduct1(Product):
    def interface(self):
        return "ConcreteProduct1 - interface"
class ConcreteProduct2(Product):
    def interface(self):
        return "ConcreteProduct2 - interface"

class creator(metaclass=abc.ABCMeta):
    # Declare the factory method, which returns an object of type Product.
    # Creator may also define a default implementation of the factory
    # method that returns a default ConcreteProduct object.
    # Call the factory method to create a Product object.
    def __init__(self):
        self.product = self.factory_method()

    @abc.abstractmethod
    def factory_method(self):
        pass
    def someOperation(self):
        #you can make some silent calls also from here
        return self.product.interface()

# Override the factory method to return an instance of a ConcreteProduct2.
class ConcreteCreator1(creator):
    def factory_method(self):
        return ConcreteProduct1()
class ConcreteCreator2(creator):
    def factory_method(self):
        return ConcreteProduct2()



def main():
    concrete_creator=ConcreteCreator1()
    print(concrete_creator.factory_method().interface())
    print(concrete_creator.product.interface())
    print(concrete_creator.someOperation())

    for cr in (ConcreteCreator1(), ConcreteCreator2()):
        print(cr.someOperation(), cr.factory_method().interface())


if __name__ == '__main__':
    main()