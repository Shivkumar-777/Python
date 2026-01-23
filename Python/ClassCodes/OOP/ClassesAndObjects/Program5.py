
class Demo:

    #class Variable

    x = 10

    def __new__(cls):

        print("In New Method")

        return super().__new__(cls)

    def __init__(self):

        print("In init : Constructor")


    def disp(self):

        print("In Disp")

obj = Demo()

print(obj.x)

obj.disp()
