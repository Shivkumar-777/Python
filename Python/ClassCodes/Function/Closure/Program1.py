
# Closure

def fun():
	x = 10
	print("Fun x : ", x)

	def gun():
		nonlocal x
		x = x + 1
		print("Gun x : ", x)

	return gun

retRef = fun()
retRef()
