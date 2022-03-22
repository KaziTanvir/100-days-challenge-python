import random as ran

in_str= input("Enter the names separated by a name and a comma \n")

op=in_str.split(", ")

#length= len(op)

#ran_index= ran.randint(0, length-1)


#print(f"{op[ran_index]} will pay the bill today")
bill=ran.choice(op)
print(f"{bill} will pay the bill")