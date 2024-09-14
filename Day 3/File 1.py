# Functions

#Block of code that performs a specific task

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp = [2100,1245,4500]
joe_exp = [200,3000,4567]

tom_total = calculate_total(tom_exp)
joe_exp= calculate_total(joe_exp)

print(tom_total)
print(joe_exp)