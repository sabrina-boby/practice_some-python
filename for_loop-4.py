

n=int(input("Enter number "))
count=0
for i in range(2,n,1):
	if n%i==0:
		count=1
		break

if count==1:
	print("not prime")
else:
    print("prime")	
