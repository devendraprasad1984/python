"""
Sequentially access the elements of a collection
promote to "full object status" the traversal of a collection.
Plymorphic traversal
Need to "abstract" the traversal of wildly different data structures so that algorithms can be defined that are capable of interfacing with each transparently.
You might also need to have more than one traversal pending on the same list." And, providing a uniform interface for traversing many types of aggregate objects (i.e. polymorphic iteration) might be valuable.
The Iterator abstraction is fundamental to an emerging technology called "generic programming". This strategy seeks to explicitly separate the notion of "algorithm" from that of "data structure". The motivation is to: promote component-based development, boost productivity, and reduce configuration management.
As an example, if you wanted to support four data structures (array, binary tree, linked list, and hash table) and three algorithms (sort, find, and merge), a traditional approach would require four times three permutations to develop and maintain. Whereas, a generic programming approach would only require four plus three configuration items.
The abstract syntax tree of Interpreter is a Composite (therefore Iterator and Visitor are also applicable).
Iterator can traverse a Composite. Visitor can apply an operation over a Composite.
Polymorphic Iterators rely on Factory Methods to instantiate the appropriate Iterator subclass.
Memento is often used in conjunction with Iterator. An Iterator can use a Memento to capture the state of an iteration. The Iterator stores the Memento internally.

"""
"""
Provide a way to access the elements of an aggregate objects equentially
without exposing its underlying representation.
"""

import collections.abc

class ConcreteIterator(collections.abc.Iterator):
    #implement an iterator interface
    def __init__(self, concrete_aggregate):
        self.concrete_aggregator_object=concrete_aggregate
    def __next__(self):
        if True: #if nothing to iterate on
            raise StopIteration
        return None

class ConcreteAggregate(collections.abc.Iterable):
    #implement the iterator creation interface to return an instance of the proper ConcreteIterator
    def __init__(self):
        self.data=None
    def __iter__(self):
        return ConcreteIterator(self)


def main():
    _ConcreteAggregate=ConcreteAggregate()
    for _ in _ConcreteAggregate:
        pass

if __name__ == '__main__':
    main()