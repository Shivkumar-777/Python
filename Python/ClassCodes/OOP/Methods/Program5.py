

class Demo:

    x = 10 

    y = 20

    def __init__(self):

        self.a = 50

        self.b = 60

    @classmethod

    def fun(cls):

        print("In Class Method")

        print(cls.x)

        print(cls.y)

    def run(self):

        print("In Instance Method")

        print(self.a)

        print(self.b)

Demo.fun()

obj = Demo()

Demo.run(obj)

obj.run()
