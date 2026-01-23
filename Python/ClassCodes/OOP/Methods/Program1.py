
class Demo:

    a = 50

    def __init__(self, x, y):

        print("Constructor")

        self.x = x

        self.y = y

    @classmethod

    def clsFun(cls):

        print("In Class Meethod")

    def instaFun(self):

        print("In Instance Method")

obj = Demo(10, 20)

obj.clsFun()

obj.instaFun()
