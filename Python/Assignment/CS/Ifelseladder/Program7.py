
percentage = float(input("Enter percentage: "))

score = float(input("Enter exam score: "))

if percentage >= 90 and score >= 90:
    print("Admission in Elite Program")
elif percentage >= 80 and score >= 70:
    print("Admission in Standard Program")
elif percentage >= 60 and score >= 50:
    print("Admission in Basic Program")
else:
    print("Not eligible")
