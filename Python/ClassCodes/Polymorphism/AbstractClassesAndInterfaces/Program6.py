from abc import ABC, abstractmethod

class Parent(ABC):

    def __init__(self):

        print("Parent Constructor")

    #@abstarctmethod

    def fun(self):

        pass

class Child:

    pass

obj = Parent()

print(type(Parent))

print(type(Child))