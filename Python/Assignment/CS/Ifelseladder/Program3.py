
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

print("Total Bill: ₹", bill)
