
# Interface

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def area(self):
        print("Area of circle")

    def perimeter(self):
        print("Perimeter of circle")


# Object creation
c = Circle()
c.area()
c.perimeter()
