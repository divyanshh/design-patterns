"""
The Flyweight Pattern is a structural design pattern that aims to minimize memory usage by sharing as much data
as possible with similar objects.
It is particularly useful when dealing with a large number of similar objects that consume a lot of memory.
The key idea is to separate the intrinsic (shared) state from the extrinsic (unique) state and store the
intrinsic state in a shared object.

Key Concepts
Flyweight: The shared object that contains intrinsic state.
Concrete Flyweight: A specific implementation of the Flyweight.
Flyweight Factory: Manages the flyweight objects and ensures that shared objects are reused.
Client: Uses the Flyweight objects.
Example Scenario
Imagine we are developing a text editor that needs to render a large number of characters.
Instead of creating a new object for each character, we can use the Flyweight pattern to share the common properties
of characters (such as font, size, and color) and store only the unique properties (such as position) separately.


Use the Flyweight pattern only when your program must support a huge number of objects which barely fit into available RAM

The benefit of applying the pattern depends heavily on how and where it’s used. It’s most useful when:
an application needs to spawn a huge number of similar objects
this drains all available RAM on a target device
the objects contain duplicate states which can be extracted and shared between multiple objects

"""

from abc import ABC, abstractmethod


# Flyweight class representing shared state
class CharacterFlyweight:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def render(self, position):
        print(f"Rendering character at {position} with font={self.font}, size={self.size}, color={self.color}")


# Flyweight Factory for creating and managing flyweights
class CharacterFlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, font, size, color):
        key = (font, size, color)
        if key not in self._flyweights:
            self._flyweights[key] = CharacterFlyweight(font, size, color)
        return self._flyweights[key]

    def list_flyweights(self):
        print(f"FlyweightFactory: {len(self._flyweights)} flyweights:")
        for key in self._flyweights:
            print(key)


# Client class representing the unique state of a character
class Character:
    def __init__(self, char, font, size, color, position, factory):
        self.char = char
        self.position = position
        self.flyweight = factory.get_flyweight(font, size, color)

    def render(self):
        print(f"Rendering character '{self.char}'")
        self.flyweight.render(self.position)


# Client code
if __name__ == "__main__":
    factory = CharacterFlyweightFactory()

    characters = [
        Character('a', 'Arial', 12, 'black', (10, 20), factory),
        Character('b', 'Arial', 12, 'black', (20, 20), factory),
        Character('a', 'Arial', 12, 'black', (30, 20), factory),
        Character('c', 'Courier', 14, 'red', (40, 20), factory),
        Character('d', 'Courier', 14, 'red', (50, 20), factory),
    ]

    for character in characters:
        character.render()

    factory.list_flyweights()
