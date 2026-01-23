

def fun(listObj):
	print("In Fun : ",listObj)
	listObj[2] = 70
	print("In Fun After Update : ", listObj)

listObj = [10, 20, 30, 40]
print("In Main : ", listObj)
fun(listObj)
print("In Main after Fun Call : ", listObj)
