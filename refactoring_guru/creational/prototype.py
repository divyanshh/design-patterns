"""
The Prototype Design Pattern is a creational design pattern that allows you to copy existing objects without making
your code dependent on their classes.
It provides a way to create new objects by cloning an existing object, known as the prototype.

Key Concepts
Prototype: The original object that is cloned to create new objects.
Clone Method: A method that creates a copy of the prototype object.

Example Scenario
Consider a scenario where you have different shapes (e.g., circles, squares) and you want to be able to clone these
shapes to create new instances. Instead of instantiating new objects from scratch, you can clone existing ones.
"""

from abc import ABC, abstractmethod
import copy


# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype - Circle
class Circle(Prototype):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle: Radius={self.radius}, Color={self.color}"


# Concrete Prototype - Square
class Square(Prototype):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Square: Side={self.side}, Color={self.color}"


# Client Code
if __name__ == "__main__":
    # Create original objects
    original_circle = Circle(10, "red")
    original_square = Square(5, "blue")

    # Clone the objects
    cloned_circle = original_circle.clone()
    cloned_square = original_square.clone()

    # Display the objects
    print(f"Original Circle: {original_circle}")
    print(f"Cloned Circle: {cloned_circle}")
    print(f"Original Square: {original_square}")
    print(f"Cloned Square: {cloned_square}")

    # Modify the cloned objects
    cloned_circle.radius = 15
    cloned_circle.color = "green"
    cloned_square.side = 10
    cloned_square.color = "yellow"

    # Display the modified clones and original objects
    print(f"Modified Cloned Circle: {cloned_circle}")
    print(f"Original Circle after modification: {original_circle}")
    print(f"Modified Cloned Square: {cloned_square}")
    print(f"Original Square after modification: {original_square}")

