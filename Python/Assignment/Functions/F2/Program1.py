

def Max(a, b, c):
	if a >= b and a >= c:
		return a
	elif b >= a and b >= c:
		return b
	else:
		return c

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

print("Maximum number is : ", Max(num1, num2, num3))
