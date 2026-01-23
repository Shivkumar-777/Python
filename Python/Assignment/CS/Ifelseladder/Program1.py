
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
hb = float(input("Enter Hb: "))

if age < 18 or age > 65:
    print("Not eligible for blood donation")
elif weight <= 50:
    print("Not eligible for blood donation")
elif hb <= 12.5:
    print("Not eligible for blood donation")
else:
    print("Eligible for blood donation")
