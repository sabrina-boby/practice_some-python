store=""
reverse=""
name=input()
store=name
print(name)
for i in range (len(name)-1,-1,-1):
	print(i)
	reverse=reverse+name[i]
print(reverse)	
