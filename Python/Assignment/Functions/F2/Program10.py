
def perfect(n):
    if n <= 0:
        return False
    
    i = 1
    sum_div = 0

    while i < n:
        if n % i == 0:
            sum_div += i
        i += 1
    
    return sum_div == n

num = int(input("Enter a number: "))

if perfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
