
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    start = rows - i + 1  # starting number for each row

    # print leading spaces
    for s in range(rows - i):
        print(" ", end=" ")

    # print numbers from start to rows
    for num in range(start, rows + 1):
        print(num, end=" ")
    print()

