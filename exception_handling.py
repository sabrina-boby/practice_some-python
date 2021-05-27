

try:
	list=[20,0,30]
	result=list[0]/list[1]
	print(result)
	print("Done")

except ZeroDivisionError:
    print("dividing zero is not possible")

except IndexError:
    print("Index Error")

finally:
    print("successful")	