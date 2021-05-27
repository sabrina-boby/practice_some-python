

# dictionary={}
# dictionary["colour"]="red"
# dictionary["name"]="rayhan + boby"
# dictionary["roll"]=101
# dictionary["section"]="B"

# for key,value in dictionary.items():
# 	print(key," : ",value)

dictionary={}

data="aabbcccc"

check = True

for i in data:
	if i in dictionary:
		dictionary[i] += 1
	else:
		dictionary[i] = 1

# for  key,value in dictionary.items():
# 	if value % 2 != 0:
# 		check = False
# 		break

for  key in dictionary:
	if dictionary[key] % 2 != 0:
		check = False
		break

if check:
	print("Beautiful")
else:
	print("Not Beautiful")
    
