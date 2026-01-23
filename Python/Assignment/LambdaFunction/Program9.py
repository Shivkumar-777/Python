
char = lambda s : 'a' in s or 'A' in s

text = input("Enter a string : ")

if char(text):
	print("The string contains 'a'.")
else:
	print("The string does not contains 'a'.")
