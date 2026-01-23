
class Animal :
    def eat(self):
        print("Animal Eats")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

p = Puppy()
p.eat()
p.bark()
p.play()
