
def product(n):
	product = 1
	i = 1

	while i <= n:
		product *= i
		i += 1

	return product

num = int(input("Enter a number : "))
print("Product = ", product(num))
