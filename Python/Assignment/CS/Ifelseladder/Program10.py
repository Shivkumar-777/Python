
a = float(input("Enter angle 1: "))
b = float(input("Enter angle 2: "))
c = float(input("Enter angle 3: "))

if a + b + c != 180:
    print("Invalid Triangle")
else:
    if a < 90 and b < 90 and c < 90:
        print("Triangle is Acute")
    elif a > 90 or b > 90 or c > 90:
        print("Triangle is Obtuse")
    else:
        print("Triangle is Right-angled")
