
def area_circle(r):
	area = 3.14 * r * r
	return area

radius = float(input("Enter radius of circle : "))
result = area_circle(radius)

print("Radius : ", radius)
print("Area Of Circle : ", result)
