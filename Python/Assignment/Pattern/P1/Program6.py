Q5.WAP for the following pattern: Take rows from the user 
Rows = 4 
4 
4  3 
4  3  2 
4  3  2  1 
Rows = 3 
3 
3  2 
3  2  1
rows = int(input("Enter no. of rows : "))

for i in range(1, rows + 1):
	for j in range(1, i +1):
        	print(j, end =" ")
	print()
	
