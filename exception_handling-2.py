



def voter(age):
	if age<18:
		raise ValueError("invalid voter")

	return "u r allow to vote"	



print(voter(17))	

