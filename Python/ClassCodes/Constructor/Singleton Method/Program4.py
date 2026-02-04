class SingletonMeta(type):

    instance = None

    def __call__(cls, *args, **kwargs):

        if cls.instance is None:

            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance

#class Demo: # Double Object

class Demo(metaclass = SingletonMeta):  # Single Object

    def __init__(self):

        print("Constructor")

obj1 = Demo()

obj2 = Demo()

print(obj1)

print(obj2)

print(type(Demo))

'''
Output :-
Constructor
<__main__.Demo object at 0x000001E2C3B1D4C0>
<__main__.Demo object at 0x000001E2C3B1DD4C0>
<class '__main__.Demo'>

'''