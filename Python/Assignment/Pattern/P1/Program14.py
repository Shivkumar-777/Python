
rows = int(input("Enter no of rows : "))

for i in range(1, rows + 1):
    print("  " * (rows - i), end="")
    for j in range(rows, rows - i, -1):
        print(j, end=" ")
    print()
