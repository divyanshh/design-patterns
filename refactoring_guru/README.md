# Creational

Creational design patterns abstract the instantiation process. 
They help make a system independent of how its objects are created, composed, and represented. 
A class creational pattern uses inheritance to vary the class that’s instantiated, whereas an object creational pattern 
will delegate instantiation to another object. 
Creational patterns give a lot of flexibility in what gets created, who creates it, how it gets created, and, when. 

There are two recurring themes in these patterns: 

They all encapsulate knowledge about which concrete class the system uses. 
They hide how instances of these classes are created and put together.

# Structural

Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. 
Structural class patterns use inheritance to compose interfaces or implementations. 
Consider how multiple inheritances mix two or more classes into one. 
The result is a class that combines the properties of its parent classes.

There are two recurring themes in these patterns: 

This pattern is particularly useful for making independently developed class libraries work together. 
Structural Design Patterns describe ways to compose objects to realize new functionality. 
The added flexibility of object composition comes from the ability to change the composition at run-time, 
which is impossible with static class composition. 

# Behavioral

Behavioral Patterns are concerned with algorithms and the assignment of responsibilities between objects. 
Behavioral patterns describe not just patterns of objects or classes but also the patterns of communication between them. 
These patterns characterize complex control flow that’s difficult to follow at run-time.

There are three recurring themes in these patterns:

Behavioral class patterns use inheritance to distribute behavior between classes. 
Behavioral object patterns use object composition rather than inheritance.
Behavioral object patterns are concerned with encapsulating behavior in an object and delegating requests to it. 
