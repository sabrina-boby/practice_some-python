temp=''
name=input()
for i in name:
	temp=name[i]
	name[i]=name[i+1]
	name[i+1]=temp
	i=i+1
print(name)
