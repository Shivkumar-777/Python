
def composite(n):
    if n <= 1:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return True
        i += 1
    
    return False

num = int(input("Enter a number: "))

if composite(num):
    print(num, "is a composite number")
else:
    print(num, "is not a composite number")
