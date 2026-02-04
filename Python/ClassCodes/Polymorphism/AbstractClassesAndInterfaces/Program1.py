
# Abstarct Class

from abc import ABC, abstractmethod

class Parent(ABC):   # Abstract Class

    def __init__(self):
        print("Parent Constructor")

    def career(self):   # Normal method
        print("Doctor")

    @abstractmethod
    def marry(self):    # Abstract method
        pass


class Child(Parent):   # Child Class

    def __init__(self):
        super().__init__()
        print("Child Constructor")

    def marry(self):    # Implementing abstract method
        print("Marry according to own choice")


# Object creation
c = Child()

c.career()
c.marry()
