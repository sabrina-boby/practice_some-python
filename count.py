

x=input("enter string ")
word=0
later=0
digit=0

for i in x:
    i=i.lower()  
    if 'a'<=i and i<='z':
        later=later+1
    elif '0'<=i and i<='9':
        digit=digit+1
    elif i==' ':
        word=word+1

print(word+1)    
print(later)  
print(digit)        