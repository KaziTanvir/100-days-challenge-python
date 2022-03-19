from re import A


print("Welcome to the Rollercoaster")

height= int(input("Enter your height in cm? "))

bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age : "))
    if age < 12:
        bill=5
        print("You have to pay $5")
    elif age <=18 :
        bill=7
        print("You have to pay $7")
    else:
        bill=13
        print("You have to pay $13")

    photo= input("Do you want a photo taken? Y or N")
    if photo =='Y' or 'y':
        bill+=3
        print(f"Your total bill is {bill}")
else:
    print("Sorry dear, you have to grow taller")