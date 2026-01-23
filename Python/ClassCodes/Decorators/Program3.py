def outerFunc(funcRef):

    def innerFunc():
        print("Start Inner Function")
        funcRef()
        print("End Inner Function")

    return innerFunc

@outerFunc
def run():
    print("In Run")

run()


'''retRef = outerFunc(run)
print(hex(id(run)))
print(retRef.__closure__)
retRef()'''

