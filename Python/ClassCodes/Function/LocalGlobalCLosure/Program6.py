
x = 10

def fun():
	
	x = 20

	print("In Fun")
	print("Local : ", x)
	print("Global : ", globals()['x'])

print(x)
fun()
print(x)
	
#print(globals())
