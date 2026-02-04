class Singleton:
    _instance = None  # Class variable

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        else:
            print("Instance already created")
        return cls._instance


# Creating objects
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Checks if both are same object

'''
Output :-
Creating new instance
Instance already created
True

'''