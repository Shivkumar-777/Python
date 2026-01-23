

def outerFunc():
	print("In Outer Function")

	def innerFunc():
		print("In Inner Function")

	return innerFunc

retVal = outerFunc()
retVal()

print(type(retVal))
