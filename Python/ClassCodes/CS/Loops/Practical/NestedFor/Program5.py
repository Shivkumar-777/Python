
rows = int(input("Enter number of rows: "))

start = 1
for i in range(rows):
    num = start
    for j in range(rows):
        print(num, end=" ")
        num += 2
    print()
    start += 4

