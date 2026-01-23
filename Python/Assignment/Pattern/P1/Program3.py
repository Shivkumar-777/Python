
rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    num = i
    for j in range(3):
        print(num, end="  ")
        num += 2
    print()

