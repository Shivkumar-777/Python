
class Demo:

    x = 10

    @classmethod

    def fun(cls):

        print("In Class Method")

        print(Demo.x)

        print(x)

Demo.fun()
