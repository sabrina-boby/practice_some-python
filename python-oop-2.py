

class student:
    roll = 0
    gpa = 0


    def __init__(self,roll,gpa):
    	self.roll=roll
    	self.gpa=gpa

    def display(self):
    	print(f"roll : {self.roll},gpa : {self.gpa}")


rahim = student(101,4.72)   
# print(isinstance(rahim,student)) 
rahim.display()



karim = student(120,4.92)   
# print(isinstance(karim,student)) 
karim.display()