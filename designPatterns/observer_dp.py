"""
A way of notifying change to a number of classes eg in db replications and in distributed computing notifying about changes to nodes or vice versa
Encapsulate the core (or common or engine) components in a Subject abstraction, and the variable (or optional or user interface) components in an Observer hierarchy.
The "View" part of Model-View-Controller.
The Observer defines a one-to-many relationship so that when one object changes state, the others are notified and updated automatically
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Chain of Responsibility passes a sender request along a chain of potential receivers. Command normally specifies a sender-receiver connection with a subclass. Mediator has senders and receivers reference each other indirectly. Observer defines a very decoupled interface that allows for multiple receivers to be configured at run-time
Mediator and Observer are competing patterns. The difference between them is that Observer distributes communication by introducing "observer" and "subject" objects, whereas a Mediator object encapsulates the communication between other objects. We've found it easier to make reusable Observers and Subjects than to make reusable Mediators.
On the other hand, Mediator can leverage Observer for dynamically registering colleagues and communicating with them.
"""
"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updatedautomatically.
"""
import abc

class Subject:
    #know its observers, any number of observer objects may observe a subject, send notificatio to its obsevers when its state changes
    def __init__(self):
        self._observers=set()
        self._subject_state=None
    def attach(self, observer):
        observer._subject=self
        self._observers.add(observer)
    def detach(self,observer):
        observer._subject=None
        self._observers.discard(observer)
    def notify(self):
        for obs in self._observers:
            obs.update(self._subject_state)
    @property
    def subject_state(self):
        return  self._subject_state
    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state=arg
        self.notify()

class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """
    def __int__(self):
        self._subject=None
        self._observer_state = None
    @abc.abstractmethod
    def update(self,args):
        pass

class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """
    def update(self, arg):
        self._observer_state = arg
        print("state changed to ",arg)
class ConcreteObserver2(Observer):
    def update(self, arg):
        self._observer_state = arg
        print("2nd state changed to ",arg)

def main():
    subject=Subject()
    subject.attach(ConcreteObserver())
    subject.attach(ConcreteObserver2())
    subject.subject_state=123
    # subject.subject_state=150

if __name__ == '__main__':
    main()