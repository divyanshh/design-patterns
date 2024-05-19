"""
The Proxy Design Pattern is a structural design pattern that provides a surrogate or placeholder for another object
to control access to it. This pattern is useful for implementing lazy initialization, access control, logging,
and other similar features.

Key Concepts
Subject: Defines the common interface for the RealSubject and the Proxy.
RealSubject: The actual object that the proxy represents.
Proxy: Controls access to the RealSubject and can add additional behavior.

Example Scenario
Consider a scenario where you have a resource-intensive object, such as a database connection.
You want to defer the creation and initialization of this object until it is actually needed.

Output of code:

Client: Executing the client code with a proxy:
Proxy: Checking access prior to firing a real request.
RealSubject: Handling request.
Proxy: Logging the time of request.

USECASE:

1. Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources
    by being always up, even though you only need it from time to time.
2. Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.
3. Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

"""

from abc import ABC, abstractmethod


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


# RealSubject
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")


# Proxy
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


# Client code
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print("Client: Executing the client code with a proxy:")
    proxy.request()
