class Demo:

    def __init__(self):
        print("Constructor")

    def __new__(cls, *args, **kwargs):
        print("Memory Allocation")
        return super().__new__(cls)

    def __call__(cls, *args, **kwargs):
        print("Call Method")

obj1 = Demo()
print(obj1)
obj1()

'''
Output :-
Memory Allocation
Constructor
<__main__.Demo object at 0x000001E2C3B1D4C0>
Call Method

'''