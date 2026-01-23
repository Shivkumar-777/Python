
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

num = 1
for i in range(rows):
    for j in range(cols):
        print(num, end=" ")
        num += 1
    print()

