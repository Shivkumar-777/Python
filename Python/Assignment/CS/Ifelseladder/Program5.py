
temp = float(input("Input temperature : "))

if temp < 0:
    print("Freezing Cold")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
elif temp <= 40:
    print("Hot")
else:
    print("Extreme Heat")
