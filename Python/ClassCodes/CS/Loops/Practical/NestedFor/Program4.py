rows = int(input("Enter rows : "))
for i in range(rows):
    num = i + 16
    for j in range(rows):
        print(num, end="\t")
        num += 3
    print()
