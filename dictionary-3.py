
dictionary={}
data="aabbccc"
ckeak = True

for i in data:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1

for key in data:
    if dictionary[key]%2!=0:
        cheak=False
        break

if cheak:
   print("beautiful")
else:
   print("not beautiful")   

