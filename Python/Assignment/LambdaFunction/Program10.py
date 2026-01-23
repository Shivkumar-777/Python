
leapYear = lambda y : (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

year = int(input("Enter a Year : "))

if leapYear(year):
	print(year, "is a leap year.")
else:
	print(year, "is not a leap year.")
