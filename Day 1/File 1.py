text = "India is my Country"
print(text)
print(text[0])
print(text[:-1])
#    text[0]='i'      String is inmutable in Python
print(text)
print(text[0:2])


# String Concatenation
s1 = "Hello"
s2 = "World"
print(s1+" "+s2)

s3 = "Hello"
s4 = 101
print(s3+" "+str(s4))   #Converting int to str


#List
items=["Apple","Orange","Mango","Banana"]
print(items)
print(items[0])
print(items[2])

items[0] = "Pineapple"   # List Updated
print(items)
print(items[:2])
print(items[-1])

#Append -- Add new items to the list
print(items)
items.append("Butter")
print(items)

#Add new items to a particular location in a list
print(items)
items.insert(1,"Lemon")
print(items)

#Join two list
country = ["India","Japan","China"]
states = ["Kerala","Delhi","Karnataka"]
joinlist = country+states
print(joinlist)

#Number of items in the list
print(len(country))
print(len(joinlist))

#Find a element in the list
"India" in states













