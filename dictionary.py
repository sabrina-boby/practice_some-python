

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]
print(x)

x = thisdict.get("year")
print(x)

thisdict["year"]=2020
print(thisdict)

for x in thisdict:
	print(x)

for x in thisdict.values():
	print(x)

for x,y in thisdict.items():
    print(x,y)	

if "year" in thisdict:
	print("Yes, year is hear")

print(len(thisdict))	

thisdict["colour"]="red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


del thisdict["year"]
print(thisdict)

#del thisdict 
#print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)



"""


clear()	    Removes all the elements from the dictionary
copy()  	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""