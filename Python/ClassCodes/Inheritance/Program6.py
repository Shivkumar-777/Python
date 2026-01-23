
# Multiple Inheritance

class Demo:
    def __init__(self):
        print("Demo Constructor")
        self.x = 10


class DemoChild1:
    def __init__(self):
        print("DemoChild1 Constructor")
        self.y = 20


class DemoChild2(Demo, DemoChild1):
    def __init__(self):
        Demo.__init__(self)
        DemoChild1.__init__(self)
        print("DemoChild2 Constructor")
        self.z = 30


obj = DemoChild2()
print(obj.x)
print(obj.y)
print(obj.z)

