
# Method Overloading 

'''
  File "Program1.py", line 14, in <module>
    obj.disp(10)
TypeError: disp() missing 1 required positional argument: 'b'
'''

class Demo:

    def __init__(self):
        print("Demo Constructor")

    def disp(self,x):
        print("First Display")

    def disp(self,a,b):
        print("Second Display")

obj = Demo()
obj.disp(10)
obj.disp(20,30)
