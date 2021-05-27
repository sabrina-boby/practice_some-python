

k=int(input())

while k!=0:
    
    n=int(input())
    if 90<=n<=100:
	    print("A+")
    elif 80<=n<90:
        print("A")	
    elif 70<=n<80:
        print("A-")    
    elif 60<=n<70:
        print("B+") 
    elif 50<=n<60:
        print("B-") 
    elif 40<=n<50:
        print("C") 
    elif 35<=n<40:
        print("D") 
    elif n<35:
        print("F")  
    k=k-1               
