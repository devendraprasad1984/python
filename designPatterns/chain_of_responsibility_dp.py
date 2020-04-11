"""
A way of passing a request between a chain of objects
Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it
Launch-and-leave requests with a single processing pipeline that contains many possible handlers.
An object-oriented linked list with recursive traversal
Make sure there exists a "safety net" to "catch" any requests which go unhandled.
Do not use Chain of Responsibility when each request is only handled by one handler, or, when the client object knows which service object should handle the request
The derived classes know how to satisfy Client requests. If the "current" object is not available or sufficient, then it delegates to the base class, which delegates to the "next" object, and the circle of life continues.
eg ATMs use this pattern, JS prototype object chaining mechanism or nested use of then().then() etc
The client "launches and leaves" each request with the root of the chain
Recursive delegation produces the illusion of magic.
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Chain of Responsibility passes a sender request along a chain of potential receivers.
Chain of Responsibility can use Command to represent requests as objects.
Chain of Responsibility is often applied in conjunction with Composite. There, a component's parent can act as its successor.
"""
"""
Avoid coupling the sender of a request to its receiver by giving
more than one object a chance to handle the request. Chain the receiving
objects and pass the request along the chain until an object handles it.
"""

import abc

class Handler(metaclass=abc.ABCMeta):
    #define interface for handling request and implement a successor link
    def __init__(self, successor=None):
        self._successor=successor

    @abc.abstractmethod
    def handle_request(self):
        pass

class ConcreteHandler1(Handler):
    #handle request else forward it to successor
    def handle_request(self):
        if self._successor is not None:
            print("inside successor of class ConcreteHandler1")
            self._successor.handle_request()
        else:
            print("ConcreteHandler1 cannot handle")

class ConcreteHandler2(Handler):
    #handle request else forward it to successor
    def handle_request(self):
        if self._successor is not None:
            print("inside successor of class ConcreteHandler2")
            self._successor.handle_request()
        else:
            print("ConcreteHandler2 cannot handle")

class ConcreteHandler3(Handler):
    #handle request else forward it to successor
    def handle_request(self):
        if self._successor is not None:
            print("inside successor of class ConcreteHandler3")
            self._successor.handle_request()
        else:
            print("ConcreteHandler3 cannot handle")

class ConcreteHandler4(Handler):
    #handle request else forward it to successor
    def handle_request(self):
        if self._successor is not None:
            print("inside successor of class ConcreteHandler4")
            self._successor.handle_request()
        else:
            print("ConcreteHandler4 cannot handle")

def main():
    concreteHandler1=ConcreteHandler1()
    concreteHandler2=ConcreteHandler2(concreteHandler1)
    concreteHandler3=ConcreteHandler3(concreteHandler2)
    concreteHandler4=ConcreteHandler4(concreteHandler3)
    # concreteHandler2.handle_request()
    # concreteHandler3.handle_request()
    concreteHandler4.handle_request()

if __name__ == '__main__':
    main()