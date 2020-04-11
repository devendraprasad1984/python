"""
Defines simplified communication between classes
Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
Design an intermediary to decouple many peers.
Identify a collection of interacting objects that would benefit from mutual decoupling.
Encapsulate those interactions in the abstraction of a new class.
Create an instance of that new class and rework all "peer" objects to interact with the Mediator only.
Balance the principle of decoupling with the principle of distributing responsibility evenly.
Be careful not to create a "controller" or "god" object.
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Chain of Responsibility passes a sender request along a chain of potential receivers. Command normally specifies a sender-receiver connection with a subclass. Mediator has senders and receivers reference each other indirectly. Observer defines a very decoupled interface that allows for multiple receivers to be configured at run-time.
Mediator and Observer are competing patterns. The difference between them is that Observer distributes communication by introducing "observer" and "subject" objects, whereas a Mediator object encapsulates the communication between other objects. We've found it easier to make reusable Observers and Subjects than to make reusable Mediators.
Mediator is similar to Facade in that it abstracts functionality of existing classes. Mediator abstracts/centralizes arbitrary communication between colleague objects, it routinely "adds value", and it is known/referenced by the colleague objects (i.e. it defines a multidirectional protocol). In contrast, Facade defines a simpler interface to a subsystem, it doesn't add new functionality, and it is not known by the subsystem classes (i.e. it defines a unidirectional protocol where it makes requests of the subsystem classes but not vice versa).
"""
"""
Define an object that encapsulates how a set of objects interact.
Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction
independently.
"""

class Mediator:
    """
    Implement cooperative behavior by coordinating Colleague objects.
    Know and maintains its colleagues.
    """
    def __init__(self):
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)

class Colleague1:
    #Know its Mediator object. Communicate with its mediator whenever it would have otherwise communicated with another colleague.
    def __init__(self, mediator):
        self._mediator = mediator
    def call(self):
        print("hi I am colleague one")
class Colleague2:
    def __init__(self, mediator):
        self._mediator = mediator
    def call(self):
        print("hi I am colleague 2")

def main():
    mediator=Mediator()
    mediator._colleague_1.call()
    mediator._colleague_2.call()

if __name__ == '__main__':
    main()
