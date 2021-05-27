

def student(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i     
    return(sum) 

x=student(10,20,30,40,50)
print("sum = ",x)




def student(**details):
    print(details["id"])

student(id=101,name="boby")
