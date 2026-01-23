

x = int(input("Enter x : "))
y = int(input("Enter y : "))

while x <= y:

    x = x + 1      # increment first

    if x % 5 == 0:
        continue   # skip printing when divisible by 5

    print(x)

print("End Code")

