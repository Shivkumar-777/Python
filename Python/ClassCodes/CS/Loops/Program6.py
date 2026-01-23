
x = int(input("Enter x : "))
y = int(input("Enter y : "))

while x < y:
#    print(x)

    if x % 5 == 0:
     #   x = x + 1     # IMPORTANT: increase x before continue to avoid infinite loop
        continue

    print(x)

    x = x + 1

print("End Code")

