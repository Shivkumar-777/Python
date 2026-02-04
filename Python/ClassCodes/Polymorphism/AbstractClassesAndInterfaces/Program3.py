
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


p1 = CreditCard()
p1.pay(500)

p2 = UPI()
p2.pay(300)

