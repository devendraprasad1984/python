"""
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
"""

import abc

class Product:
    #representing the complex object under construction
    pass

class Builder(metaclass=abc.ABCMeta):
    #specify an abstract interface for creating parts of product object
    def __init__(self):
        self.product=Product()
    @abc.abstractmethod
    def _build_part_a(self):
        pass
    @abc.abstractmethod
    def _build_part_b(self):
        pass
    @abc.abstractmethod
    def _build_part_c(self):
        pass

class ConcereteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """
    def _build_part_a(self):
        return "product part _build_part_a"
    def _build_part_b(self):
        return "product part _build_part_b"
    def _build_part_c(self):
        return "product part _build_part_c"

class Director:
    #construct the object using builder interace
    def __init__(self):
        self._builder=None
    def construct(self,builder):
        self._builder=builder
        a=self._builder._build_part_a()
        b=self._builder._build_part_b()
        c=self._builder._build_part_c()
        return [a,b,c]

def main():
    concrete_builder=ConcereteBuilder()
    director=Director()
    xbld=director.construct(concrete_builder)
    print(xbld)
    product=concrete_builder.product

if __name__ == '__main__':
    main()