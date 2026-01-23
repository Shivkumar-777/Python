
rows = int(input("Enter no. rows : "))

for i in range(1, rows+1):
    for j in range(3):
        if i % 3 == 0:
            print("#", end="\t")
        elif i % 3 == 1:
            print("$", end="\t")
        else:
            print("@", end="\t")
    print()

