
rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = i * rows + 1
    for j in range(rows):
        print(num, end=" ")
        num += 2
    print()

