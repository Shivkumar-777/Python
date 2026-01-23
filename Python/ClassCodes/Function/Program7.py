'''def fun(*args, **kwargs):

    for i in args:
        print(i)

    for i, j in kwargs.items():
        print(i, ":", j)

fun(10, 20, 30, jerNo=18, pName="Virat", runs=50000)

fun(10, 20, 30, jerNo=18, pName="Virat", runs=50000, 40, 50, 60)   # THIS IS WRONG'''

def fun(*args, **kwargs):

    for i in args:
        print(i)

    for i, j in kwargs.items():
        print(i, ":", j)


# valid function calls

fun(10, 20, 30, jerNo=18, pName="Virat", runs=50000)

fun(10, 20, 30, 40, 50, 60, jerNo=18, pName="Virat", runs=50000)


