
x = 30

def fun():
	global x
	x = x + 1
	print("In Fun")
	print("In Fun :", x)

print(x)
fun()
print(x)
