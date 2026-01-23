
def decorFun(funRef):

    def innerFun(*args, **kwargs):

        print("Start Decoration")

        funRef(*args, **kwargs)

        print("End Decoration")

    return innerFun

@decorFun

def add(x,y):

    print("x : ", x)

    print("y : ", y)

    print("Add : ", x+y)

add(10, 20)
