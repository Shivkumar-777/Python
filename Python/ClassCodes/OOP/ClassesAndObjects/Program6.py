'''

class Demo:

    pass

obj = Demo()

'''

class Demo:

    def __new__(cls):

        print("Memory Allocation")

        return super().__new__(cls)

    def __init__(self):

        print("Constructor")

obj = Demo()

#obj = __new__(Demo)     Memory Location
#__init__(obj)           Instance Variable Intilization
