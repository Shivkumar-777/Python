
class Demo : 

    def __init__(self):
        self.x = 10
        self.y = 20
        self.__z = 30

obj = Demo()

print(obj.__dict__)

print(obj.x)
print(obj.y)
#print(obj._Demo__z)
print(obj.__z)
