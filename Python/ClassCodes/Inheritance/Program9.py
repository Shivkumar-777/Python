
class Vehicle :
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    def ride(self):
        print("Bike is running")

b = Bike()
b.start()
b.ride()
