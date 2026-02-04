class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\n--- Student Details ---")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)


# Taking input from user
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

# Creating object using constructor
s1 = Student(name, age, marks)

# Displaying details
s1.display()

'''
Output :-

Enter student name: Shiv
Enter age: 20
Enter marks: 93

--- Student Details ---
Name : Shiv
Age  : 20
Marks: 93.0

'''