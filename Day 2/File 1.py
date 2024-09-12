# For loop

#Store monthly expenses in a list and find out total expenses for all months

exp = [2345,2666,2333,4555,2678,3456]
#traditional way total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]+exp[5]
total = 0
for item in exp:
    total = total + item
print(total)
