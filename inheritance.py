
class  A:
    def display1(self):
        print("I am from A class")


class  B(A):
    def display2(self):
        print("I am from B class")


class  C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am from C class")      


ob1=A()
ob1.display1()

ob2=B()
ob2.display1()
ob2.display2()

ob3=C()
ob3.display3()