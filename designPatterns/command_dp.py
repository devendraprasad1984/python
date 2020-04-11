"""
Encapsulate a command request as an object, thereby letting you parametrize clients with different requests, queue or log requests, and support undoable operations.
Promote "invocation of a method on an object" to full object status
An object-oriented callback
Need to issue requests to objects without knowing anything about the operation being requested or the receiver of the request.
Command decouples the object that invokes the operation from the one that knows how to perform it
The client that creates a command is not the same client that executes it.
All clients of Command objects treat each object as a "black box" by simply invoking the object's virtual  execute() method whenever the client requires the object's "service".
use java reflection or c++pointers to member function
Command objects can be thought of as "tokens" that are created by one client that knows what need to be done, and passed to another client that has the resources for doing it.
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Command normally specifies a sender-receiver connection with a subclass.
Chain of Responsibility can use Command to represent requests as objects.
Command and Memento act as magic tokens to be passed around and invoked at a later time. In Command, the token represents a request; in Memento, it represents the internal state of an object at a particular time. Polymorphism is important to Command, but not to Memento because its interface is so narrow that a memento can only be passed as a value.
Command can use Memento to maintain the state required for an undo operation.
MacroCommands can be implemented with Composite.
A Command that must be copied before being placed on a history list acts as a Prototype.
Two important aspects of the Command pattern: interface separation (the invoker is isolated from the receiver), time separation (stores a ready-to-go processing request that's to be stated later).
"""
"""
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
"""
import abc

class invoker:
    #ask the command to carry out requests
    def __init__(self):
        self._commands=[]
    def store_command(self, command):
        self._commands.append(command)
    def execute_commands(self):
        for cmd in self._commands:
            cmd.execute()

class Command(metaclass=abc.ABCMeta):
    #declare an interface for executing operations
    def __init__(self, receiver):
        self._receiver=receiver
    @abc.abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    #define building between a receiver object and an action
    #implement execute bu invoking corresponding operation(s) on receiver
    def execute(self):
        self._receiver.action()

class Receiver:
    #know how to perform the operations associated with carrying out a request. any class may server as a receiver
    def action(self):
        print("----action in receiver been performed")
class Receiver2:
    #know how to perform the operations associated with carrying out a request. any class may server as a receiver
    def action(self):
        print("----second action in receiver2 has been performed")
class Receiver3:
    #know how to perform the operations associated with carrying out a request. any class may server as a receiver
    def action(self):
        print("----third action in receiver3 has been performed")

def main():
    _invoker=invoker()

    print("from classic command pattern")
    _invoker.store_command(ConcreteCommand(Receiver()))
    _invoker.store_command(ConcreteCommand(Receiver2()))
    _invoker.store_command(ConcreteCommand(Receiver3()))

    _invoker.execute_commands()

    print("from simple command pattern and object rotator")
    #dummy dp
    obj_receivers=[Receiver(),Receiver2(),Receiver3()]
    for rec in obj_receivers:
        rec.action()



if __name__ == '__main__':
    main()