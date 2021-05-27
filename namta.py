

def namta(a=1,i=1):
    return a*i

a=int(input("Enter numb = "))
for i in range(1,11):
    print(a," * ",i," = ",namta(a*i))
   