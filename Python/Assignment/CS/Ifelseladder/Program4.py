
income = float(input("Enter Anual Income : "))

if income <= 250000:
	tax = 0,"No tax"
elif income <= 500000:
	tax = (income - 250000) * 0.05
elif income <= 1000000:
	tax = (income - 250000) * 0.20
else:
	tax = (income - 250000) * 0.30

print("Tax to be paid : ", tax)
