'''
rows = int(input("Enter rows: "))

for i in range(1, rows+1):
    for num in range(rows, rows - i, -1):
        print(num, end="  ")
    print()
'''

rows = int(input("Enter rows: "))

for i in range(1, rows+1):
    num = rows
    for j in range(i):
        print(num, end="  ")
        num -= 1
    print()

