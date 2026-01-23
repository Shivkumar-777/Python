
def outer():
	x = 10

	def inner():
		return x + 5
	return inner()

print(outer())
