"""
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in chain.

Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various
ways, but the exact types of requests and their sequences are unknown beforehand.

The Chain of Responsibility pattern is used to pass a request along a chain of potential handlers until one of them
handles the request. It decouples the sender and receiver of a request, allowing multiple objects to handle the request
without the sender knowing which object will handle it.

Decorator helps adding functionalities at runtime

APPLICATION:

The pattern lets you link several handlers into one chain and, upon receiving a request, “ask” each handler whether it
can process it. This way all handlers get a chance to process the request.

Use the pattern when it’s essential to execute several handlers in a particular order.
Since you can link the handlers in the chain in any order, all requests will get through the chain exactly as you planned.

Key Concepts
Handler: Defines an interface for handling requests and for setting the next handler in the chain.
ConcreteHandler: Implements the Handler interface and handles the request if possible.
 Otherwise, it passes the request to the next handler in the chain.
Client: Initiates the request to the chain.

Example Scenario
Imagine a scenario where a support system needs to handle customer support tickets.
Different levels of support staff handle different types of requests.
For example, Level 1 support handles basic requests, Level 2 support handles more complex requests, and Level 3 support
handles the most complex requests.
"""

from abc import ABC, abstractmethod


# Handler Interface
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


# Concrete Handler - Level1Support
class Level1Support(Handler):
    def handle(self, request):
        if request == "basic":
            print("Level 1 support handled the request.")
        elif self._next_handler:
            self._next_handler.handle(request)


# Concrete Handler - Level2Support
class Level2Support(Handler):
    def handle(self, request):
        if request == "intermediate":
            print("Level 2 support handled the request.")
        elif self._next_handler:
            self._next_handler.handle(request)


# Concrete Handler - Level3Support
class Level3Support(Handler):
    def handle(self, request):
        if request == "complex":
            print("Level 3 support handled the request.")
        elif self._next_handler:
            self._next_handler.handle(request)


# Client Code
if __name__ == "__main__":
    # Create handlers
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()

    # Set up the chain of responsibility
    level1.set_next(level2).set_next(level3)

    # Client requests
    requests = ["basic", "intermediate", "complex", "unknown"]

    for request in requests:
        print(f"\nClient: Who can handle a '{request}' request?")
        level1.handle(request)
