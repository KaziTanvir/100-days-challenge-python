from re import S


print("Welcome to pizza hut")

size= input("What size would you like? S, M or L   ")
pepper= input("Do you want to add pepperoni? Y or N  ")
cheese= input("Do you want to add extra cheese? Y or N  ")

bill=0

if size == 'S' or size == 's':
    bill +=15
elif size == 'M' or size == 'm':
    bill += 20
else:
    bill += 25 

if cheese == 'Y' or cheese == 'y':
    bill +=1
else:
    bill +=0

if pepper == 'Y' or pepper == 'y':
    if size == 'S' or size == 's':
        bill += 2
    else:
        bill +=3
 
print(f"Your total bill is ${bill}")