"""
Alter an object's behavior when its state changes
wrapper + polymorphic wrappee + collaboration
Define a "context" class to present a single interface to the outside world.
Define a State abstract base class.
Represent the different "states" of the state machine as derived classes of the State base class.
Define state-specific behavior in the appropriate State derived classes.
Maintain a pointer to the current "state" in the "context" class.
To change the state of the state machine, change the current "state" pointer.
eg vending machines behaviours based on run time entry
State objects are often Singletons.
Flyweight explains when and how State objects can be shared.
Interpreter can use State to define parsing contexts.
Strategy is a bind-once pattern, whereas State is more dynamic
The structure of State and Bridge are identical (except that Bridge admits hierarchies of envelope classes, whereas State allows only one). The two patterns use the same structure to solve different problems: State allows an object's behavior to change along with its state, while Bridge's intent is to decouple an abstraction from its implementation so that the two can vary independently.
The implementation of the State pattern builds on the Strategy pattern. The difference between State and Strategy is in the intent. With Strategy, the choice of algorithm is fairly stable. With State, a change in the state of the "context" object causes it to select from its "palette" of Strategy objects.
"""

"""
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.
"""

import abc

class Context:
    #Define the interface of interest to clients. Maintain an instance of a ConcreteState subclass that defines the current state.
    def __init__(self, state):
        self._state=state
    def setContext(self,state):
        self._state=state
    def request(self):
        self._state.handle()

class State(metaclass=abc.ABCMeta):
    #Define an interface for encapsulating the behavior associated with a particular state of the Context.
    @abc.abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    #Implement a behavior associated with a state of the Context.
    def handle(self):
        print("Concrete State A has been called")

class ConcreteStateB(State):
    def handle(self):
        print("Concrete State B has been called of")

def main():
    context=Context(ConcreteStateA())
    context.request()
    context=Context(ConcreteStateB())
    context.request()
    context.setContext(ConcreteStateA())
    context.request()

if __name__ == '__main__':
    main()

