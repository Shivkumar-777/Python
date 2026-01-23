
rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = i + 1  # start value for each row
    for j in range(i + 1):
        print(num * (j + 1), end=" ")
    print()

