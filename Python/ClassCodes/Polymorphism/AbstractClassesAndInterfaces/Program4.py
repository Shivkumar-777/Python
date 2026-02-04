
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def interest(self):
        pass


class SavingsAccount(Account):
    def interest(self):
        print("Savings Account Interest: 4%")


class CurrentAccount(Account):
    def interest(self):
        print("Current Account Interest: 0%")


a1 = SavingsAccount()
a2 = CurrentAccount()

a1.interest()
a2.interest()

