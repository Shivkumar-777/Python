class Demo:

    instance = None

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:   # FIXED
            print("Memory Allocation")
            cls.instance = super().__new__(cls)

        return cls.instance


obj1 = Demo()   # FIXED
obj2 = Demo()

print(obj1 is obj2)

'''
Output :-
Memory Allocation
True

'''