
rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1
    
    # Print spaces
    for s in range(i):
        print(" ", end=" ")
    
    # Print numbers
    for j in range(rows - i):
        print(num, end=" ")
        num += 1
    
    print()

