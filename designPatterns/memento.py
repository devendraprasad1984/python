"""
Capture and restore an object's internal state
Without violating encapsulation, capture and externalize an object's internal state so that the object can be returned to this state later.
A magic cookie that encapsulates a "check point" capability.
Promote undo or rollback to full object status.
defines three distinct roles:
Originator - the object that knows how to save itself.
Caretaker - the object that knows why and when the Originator needs to save and restore itself.
Memento - the lock box that is written and read by the Originator, and shepherded by the Caretaker.
Command and Memento act as magic tokens to be passed around and invoked at a later time. In Command, the token represents a request; in Memento, it represents the internal state of an object at a particular time. Polymorphism is important to Command, but not to Memento because its interface is so narrow that a memento can only be passed as a value.
Command can use Memento to maintain the state required for an undo operation.
Memento is often used in conjunction with Iterator.

"""

"""
Capture and externalize an object's internal state so that the object
can be restored to this state later, without violating encapsulation.
"""

import pickle

class Originator:
    """
    Create a memento containing a snapshot of its current internal
    state.
    Use the memento to restore its internal state.
    """

    def __init__(self):
        self._state = None

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def create_memento(self):
        return pickle.dumps(vars(self))


def main():
    originator = Originator()
    memento = originator.create_memento()
    originator._state = True
    originator.set_memento(memento)


if __name__ == "__main__":
    main()