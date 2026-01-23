
rows = int(input("Enter number of rows: "))

num = 4  # starting number given in pattern

for i in range(1, rows + 1):
    # print leading spaces
    for s in range(rows - i):
        print("   ", end="")  # alignment

    # print continuous numbers
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

