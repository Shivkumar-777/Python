
rows = int(input("Enter no. of rows : "))

for i in range(rows):
	num = 1
	for j in range(rows):
		print(num, end = " ")
		num += 2
	print()
