
class shape:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b

class triangle(shape):
    def area(self):
        area=0.5*self.a*self.b
        print("area of triangle = ",area)

class rectengle(shape):
    def area(self):
        area=self.a*self.b
        print("area of rectengle = ",area)      



t=triangle(10,20)  
t.area()
r=rectengle(10,20)
r.area()
