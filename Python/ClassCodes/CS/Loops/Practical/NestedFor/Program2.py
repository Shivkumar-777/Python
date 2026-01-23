
rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1
    for j in range(rows):
        print(num, end="\t")
        num += 2
    print()

