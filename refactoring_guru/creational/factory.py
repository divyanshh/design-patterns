from abc import ABC, abstractmethod


# Abstract Product
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


# Concrete Products
class Car(Vehicle):
    def move(self):
        return "Car is moving on the road."


class Bike(Vehicle):
    def move(self):
        return "Bike is moving on the road."


# Factory
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Invalid vehicle type")


# Client code
vehicle1 = VehicleFactory.create_vehicle("car")
print(vehicle1.move())  # Output: Car is moving on the road.

vehicle2 = VehicleFactory.create_vehicle("bike")
print(vehicle2.move())  # Output: Bike is moving on the road.
