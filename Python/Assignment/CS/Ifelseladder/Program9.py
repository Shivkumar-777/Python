
amount = float(input("Enter purchase amount : "))

if amount < 1000:
    discount = 0
elif amount <= 4999:
    discount = 5
elif amount <= 9999:
    discount = 10
elif amount <= 19999:
    discount = 20
else:
    discount = 30

final_amount = amount - (amount * discount / 100)

print("Discount Applied:", str(discount) + "%")
print("Final Amount: ₹" + str(final_amount))
