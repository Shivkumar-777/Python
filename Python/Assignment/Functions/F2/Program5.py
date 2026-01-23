
def AvgMarks():
	total = 0
	i = 1

	while i <= 5:
		mark = int(input("Enter marks of subject " + str(i) + " : "))
		total += mark
		i += 1

	return total / 5

avg = AvgMarks()
print("Average Marks = ", avg)


