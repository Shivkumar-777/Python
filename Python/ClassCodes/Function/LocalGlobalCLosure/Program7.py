
x = 10

def fun():

	x = 20

	print("Fun : ", x)
	
	def gun():

		nonlocal x #global x

		x = x + 1
		print("Gun x : ", x)

	return gun

print(x)

retVal = fun()

retVal()

print(x)
