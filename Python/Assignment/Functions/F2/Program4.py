
def Sum(start, end):
	total = 0
	i = start

	while i <= end:
		total += i
		i += 1

	return total

start = int(input("Enter start number : "))
end = int(input("Enter end number :"))

print("Sum : ", Sum(start, end))

