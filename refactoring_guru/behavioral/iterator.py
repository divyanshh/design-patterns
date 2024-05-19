"""
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying
representation (list, stack, tree, etc.).

The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object
(such as a list) sequentially without exposing its underlying representation.
It allows sequential traversal of elements without needing to know the underlying data structure.

Key Concepts
Iterator: Provides a way to access elements of an aggregate object sequentially without exposing its underlying structure.
Aggregate: Defines an interface for creating an Iterator object.
Concrete Iterator: Implements the Iterator interface and keeps track of the current position in the aggregate.
Example Scenario
Imagine you have a custom collection class that holds a list of items, and you want to provide a way to iterate over
these items without exposing the list directly.

"""

from abc import ABC, abstractmethod


# Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# Concrete Iterator
class ListIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()


# Aggregate Interface
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


# Concrete Aggregate
class ListAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return ListIterator(self._items)


# Client Code
if __name__ == "__main__":
    aggregate = ListAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    print("Iterating over the collection:")
    while iterator.has_next():
        item = iterator.next()
        print(item)


"""
Explanation
Iterator (Iterator): Abstract base class defining the interface for iterators.
ListIterator (Concrete Iterator): Implements the iterator interface to traverse a list.
Aggregate (Aggregate): Abstract base class defining the interface for creating iterators.
ListAggregate (Concrete Aggregate): Implements the aggregate interface and provides a way to create an iterator over a list.
Client Code: Creates an aggregate, adds items to it, and iterates over the items using the iterator.
"""
