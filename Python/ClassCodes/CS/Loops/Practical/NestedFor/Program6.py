
rows = int(input("Enter number of rows: "))

num = 1
for i in range(rows):
    for j in range(rows):
        print(num, end=" ")
        num += 2
    num = num - (rows * 2) + 1
    print()

