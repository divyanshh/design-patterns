"""
The Decorator Design Pattern is a structural design pattern used to add new behavior to objects dynamically.
This pattern allows behavior to be added to individual objects, either statically or dynamically, without
affecting the behavior of other objects from the same class.

Key Concepts
Component: The original object that needs to be decorated.
Decorator: An abstract class or interface that wraps the component.
Concrete Decorators: Classes that extend the functionality of the component by adding new behavior.
Example Scenario
Imagine you have a simple notification system that sends notifications. You want to extend this system to add more
functionalities like sending notifications via email, SMS, and Slack without altering the existing notification classes.

This pattern is useful when you want to extend the functionalities of objects in a flexible and reusable way.
Decorators provide an alternative to subclassing for extending behavior, promoting a composition over
inheritance approach.

"""


from abc import ABC, abstractmethod


# Component Interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Concrete Component
class BasicNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending basic notification: {message}")


# Base Decorator
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str):
        self._notifier.send(message)


# Concrete Decorator for Email Notifications
class EmailNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_email(message)

    def send_email(self, message: str):
        print(f"Sending email notification: {message}")


# Concrete Decorator for SMS Notifications
class SMSNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_sms(message)

    def send_sms(self, message: str):
        print(f"Sending SMS notification: {message}")


# Concrete Decorator for Slack Notifications
class SlackNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_slack(message)

    def send_slack(self, message: str):
        print(f"Sending Slack notification: {message}")


# Client code
if __name__ == "__main__":
    notifier = BasicNotifier()
    notifier = EmailNotifier(notifier)
    notifier = SMSNotifier(notifier)
    notifier = SlackNotifier(notifier)

    notifier.send("Hello, world!")
