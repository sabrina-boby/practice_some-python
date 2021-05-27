
data = '[{()}]'



dictionary={}

flage=0

for i in data:
	if i in dictionary:
		dictionary[i]=dictionary[i]+1
	else:
		dictionary[i]=1


# if dictionary['['] != dictionary[']']:
# 	flage=0
# elif dictionary['('] != dictionary[')']:
# 	flage=0
# elif dictionary['{'] != dictionary['}']:
#     flage=0	


# if dictionary['['] == dictionary[']']:
# 	flage=1
# if dictionary['('] == dictionary[')']:
# 	flage=flage+1
# if dictionary['{'] == dictionary['}']:
#     flage=flage+1
	


if dictionary['['] == dictionary[']']:
	if dictionary['('] == dictionary[')']:
		if dictionary['{'] == dictionary['}']:
			flage=1

if flage:
   print("beautyful")
else:
   print("not beautyful")   		
