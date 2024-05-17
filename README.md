# Design-patterns

## Creational patterns

Creational design patterns are design patterns that deal with object creation mechanisms, 
trying to create objects in a manner suitable to the situation.
The basic form of object creation could result in design problems or added complexity to the design. 
Creational design patterns solve this problem by somehow controlling this object creation.


Factory Design Pattern:

1. The Factory pattern is a creational pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. 
2. It defines an interface for creating an object but allows the subclasses to decide which class to instantiate. 
3. This pattern is useful when you have a superclass with multiple subclasses and you want to instantiate one of them based on some parameter. 
4. Example: Consider a VehicleFactory that can create different types of vehicles like Car, Bike, Truck, etc.

Abstract Factory Design Pattern:

1. The Abstract Factory pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. 
2. It is used when there are multiple families of products, and the system needs to be independent of how these products are created, composed, and represented. 
3. It provides an interface for creating families of related or dependent objects without specifying their concrete classes. 
4. Example: Suppose you're building a GUI library. You might have factories for creating different types of buttons, text fields, and windows for different operating systems like Windows, macOS, and Linux.

