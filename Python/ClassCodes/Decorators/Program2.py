
def fun(x):
    print(x)
    x()

def run():
    print("In Run")

fun(run)
