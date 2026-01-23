day = input("Enter day : ")

match day:
    case "Mon" | "Monday":
        print("Start Of the Week")
    case "Fri" | "Friday":
        print("Weekend is coming")
    case "Sat" | "Saturday":
        print("Weekend Start")
    case "Sun" | "Sunday":
        print("Relax, it's Sunday")
    case _:
        print("Yet Another Day")
