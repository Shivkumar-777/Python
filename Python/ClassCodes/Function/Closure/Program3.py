
x = 10

def fun():
	x = 20
	print("Fun x : ", x)

	def gun():
		nonlocal x
		x = x + 1
		print("Gun x : ", x)

		def run():
			print("Run x : ", x)

		return run

	return gun

retGun = fun()
retRun = retGun()
retRun()
print(x)
