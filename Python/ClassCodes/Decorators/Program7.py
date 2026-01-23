
def decorFun1(funRef1):

    def innerFun1():

        print("Start Decoration1")

        funRef1()

        print("End Decoration1")

    return innerFun1

def decorFun2(funRef2):

    def innerFun2():

        print("Start Decoration2")

        funRef2()

        print("End Decoration2")

    return innerFun2


@decorFun1

@decorFun2

def fun():

    print("In Fun")

fun()
