
def fun(x):
	print("In fun Before : ", x)
	x = 30
	print("In fun After : ", x)

x = 10
print("Global Before : ", x)
fun(x)
print("Global After : ", x)
