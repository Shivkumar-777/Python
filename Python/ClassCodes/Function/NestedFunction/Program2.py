
def OuterFunc():
    print("In Outer Function")

    def InnerFunc():
        print("In Inner Function")

    InnerFunc()
    print("End Outer")

OuterFunc()


