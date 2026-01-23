
def fun():
	x = 10
	#print(hex(id(x)))
	print("Fun x : ", x)

	def gun():
		print("Gun x : ", x)

	return gun

retRef = fun()
retRef()
print(retRef.__closure__[0].cell_contents)
