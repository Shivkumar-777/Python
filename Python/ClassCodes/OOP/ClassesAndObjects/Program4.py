
class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


    def display(self):
        print(self.name, self.roll)

s1 = Student("Kanha :", 101)
s1.display()
