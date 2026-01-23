

# Keywordargs

def fun(**data):
	for i,j in data.items():
		print(i, ":", j)

fun(Name = "Shiv",Age = 20, City="Pune")
