"""
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
"""

import abc


class Target(metaclass=abc.ABCMeta):
    # define domain specific interface that client uses
    def __init__(self, cls):
        self._adaptee = cls

    @abc.abstractmethod
    def request(self):
        pass


# Define an existing interface that needs adapting.
class Adaptee:
    def specific_req(self):
        print("specific req has been catered - adaptee1")
        pass


class Adaptee2:
    def specific_req(self):
        print("specific req has been catered - adaptee2")
        pass


# Adapt the interface of Adaptee to the Target interface.
class Adapter(Target):
    def __init__(self, cls):
        # print("object is of Adaptee class",isinstance(cls,Adaptee))
        super().__init__(cls)

    def request(self):
        self._adaptee.specific_req()


def main():
    Adapter(Adaptee()).request()
    Adapter(Adaptee2()).request()


if __name__ == '__main__':
    main()
