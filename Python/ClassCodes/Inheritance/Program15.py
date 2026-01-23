
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    def show(self):
        print("C")
        super().show()

obj = C()
obj.show()


