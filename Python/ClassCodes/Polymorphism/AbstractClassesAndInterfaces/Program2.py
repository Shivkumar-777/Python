
from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class

    @abstractmethod
    def start(self):   # Abstract method
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

# v = Vehicle()  ERROR (cannot create object)

c = Car()
c.start()

