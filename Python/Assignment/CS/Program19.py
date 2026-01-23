
char1 = input("Enter first character: ")
char2 = input("Enter second character: ")

ascii1 = ord(char1)
ascii2 = ord(char2)

if ascii1 % 2 != 0 and ascii2 % 2 != 0:
    print(ascii1 + ascii2)
else:
    print("sum is odd")
