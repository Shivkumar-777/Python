
class Demo:

    x = 10

    def __init__(self):

        self.y = 20

    @classmethod

    def fun(cls):

        print("In Class Method")

        print(Demo.x)

        print(cls.x)

Demo.fun()

obj = Demo()

obj.fun()
