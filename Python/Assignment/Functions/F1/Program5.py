
def check(ch):
	if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
		print(ch, "is a Vowel")
	else:
		print(ch, "is a Consonant")

char = input("Enter a Character : ")
check(char)
