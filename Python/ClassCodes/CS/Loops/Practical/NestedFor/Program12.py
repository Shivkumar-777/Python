
rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = rows
    for j in range(rows - i):
        print(num, end=" ")
        num -= 1
    print()

