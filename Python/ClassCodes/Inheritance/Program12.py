
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def circle_info(self):
        print("This is a circle")

class Square(Shape):
    def square_info(self):
        print("This is a square")

c = Circle()
s = Square()

c.draw()
c.circle_info()

s.draw()
s.square_info()

