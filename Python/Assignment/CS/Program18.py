
char1 = input("Enter a character: ")

ascii_value = ord(char1)   # convert character to ASCII value

if ascii_value % 2 == 0:
    print(char1)
else:
    print("odd")
