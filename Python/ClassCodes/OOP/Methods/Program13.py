
class Outer:

    a = 50

    def __init__(self):
        print("Outer Constructor")
        self.b = 60

    class Inner:

        x = 10

        def __init__(self, outer_obj):
            print("Inner Constructor")
            self.y = 20
            self.outer = outer_obj   # store outer object reference

        def innerFun(self):
            print("Inner Instance Method")
            print(self.x)           # Inner class variable
            print(self.y)           # Inner instance variable
            print(Outer.a)          # Outer class variable
            print(self.outer.b)     # Outer instance variable

    def outerFun(self):
        print("Outer Instance Method")


obj = Outer()
obj.outerFun()

obj2 = Outer.Inner(obj)
obj2.innerFun()

