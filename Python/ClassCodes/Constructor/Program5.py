class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"\n{self.brand} car runs at {self.speed} km/h")


brand = input("Enter car brand: ")
speed = int(input("Enter speed: "))

c1 = Car(brand, speed)
c1.show()

'''
Output :-
Enter car brand: Toyota
Enter speed: 180
Toyota car runs at 180 km/h

'''
