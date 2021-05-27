a=""
b=""
c=""
d=""
name=input()
for i in name:
	if 'A'<=i and i<='Z':
	    a=a+i
	elif 'a'<=i and i<='z':
	    b=b+i
	elif '0'<=i and i<='9':
	    c=c+i    
	else :
	    d=d+i    
print(a)
print(b)
print(c)
print(d)
