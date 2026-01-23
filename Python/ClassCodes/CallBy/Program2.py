
def fun(x,y):
	print("Fun Data : ", x,y)
	x = 50
	y = 100
	print("Fun data after update : ", x,y)

x = 10
y = 20
print("Main Data : ", x,y)
fun(x,y)
print("Main data after fun call : ", x,y)
