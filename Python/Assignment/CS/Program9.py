
val = input("Enter char : ")

if len(val) == 1:
    if val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u' or \
       val == 'A' or val == 'E' or val == 'I' or val == 'O' or val == 'U':
        print(val, "is vowel")
    elif 'a' <= val <= 'z' or 'A' <= val <= 'Z':
        print(val, "is consonant")
    else:
        print(val, "is special character")
else:
    print("Please enter only one character")
