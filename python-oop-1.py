

class student:
    roll = ""
    gpa = ""


    def set_value(self,roll,gpa):
    	self.roll=roll;
    	self.gpa=gpa;

    def display(self):
    	print(f"roll : {self.roll},gpa : {self.gpa}")


rahim = student()   
# print(isinstance(rahim,student)) 
rahim.set_value(101,4.72)
rahim.display()



karim = student()   
# print(isinstance(karim,student)) 
karim.set_value(120,4.92)
karim.display()