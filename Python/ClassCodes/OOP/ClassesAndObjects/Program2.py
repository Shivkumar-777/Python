
a = 50

class Demo:

    x = 10

    def disp(self):
        print("x :",Demo.x)


def fun():
    print("In Fun")

print(a)
fun()

obj = Demo()
obj.disp()
#Demo.disp()

print(Demo.x)
