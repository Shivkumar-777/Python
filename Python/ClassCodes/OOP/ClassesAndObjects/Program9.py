
class Demo:

    x = 10

    def __init__(self):

        print("In Constructor")

        self.a = 20

        self.b = 30

obj = Demo()

#Class Variable Access

print(Demo.x)

print(obj.x)

#instance variable

print(obj.a)

print(obj.b)

print(Demo.a)

print(Demo.b)
