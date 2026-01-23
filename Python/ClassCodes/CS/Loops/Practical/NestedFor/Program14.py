rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    num = i   # starting number = row number

    # print leading spaces
    for s in range(rows - i):
        print(" ", end=" ")

    # print numbers
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

