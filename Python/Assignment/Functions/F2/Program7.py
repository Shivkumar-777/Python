
def factorial(n):
    fact = 1
    i = 1
    
    while i <= n:
        fact *= i
        i += 1
    
    return fact

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)
