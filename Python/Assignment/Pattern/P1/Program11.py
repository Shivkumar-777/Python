
rows = int(input("Enter no. of rows : "))

for i in range(rows, 0, -1):
    print("  " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

