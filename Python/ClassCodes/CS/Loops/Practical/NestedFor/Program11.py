
rows = int(input("Enter number of rows: "))
num = 1

for i in range(rows):
    num = 1
    for j in range(rows - i):
        print(num, end=" ")
        num += 1
    print()

