#[{()}]
dictionary={}
# data1="{"
# data2="}"
# data3="["
# data4="]"
# data5="("
# data6=")"
n=int(input())

check=True
for i in n:
	data=input("")
	if data in dictionary:
		dictionary[i]=dictionary[i]+1
	else:
	    dictionary[i]=1


for key in dictionary:
	if(dictionary[i]%2!=0):
		check=False
	print(dictionary)


if check:
   print("beautyful")
else:
   print("not beautyful")   		
