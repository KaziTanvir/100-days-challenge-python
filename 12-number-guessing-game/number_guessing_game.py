def no_of_terms(choice):
    if choice == "easy":
        return 10
    else:
        return 5

def check(num, user):
    if num== user:
        print("Your guess is right")
        return True
    elif user>num:
        print("Too High \nGuess again")
        return False
    else:
        print("Too low \nGuess Again")
        return False

import os
from art import logo
import random as rand
print(logo)
print("---------------------------------------------------------------------")
end_check= False
end_check2= False
cont= 0
while not end_check:
    print("Welcome to the number guessing game")
    print("I am thinking of a number in between 1 and 100")
    number=rand.randint(0,101)
    difficulty= input("Choose a difficulty. Type 'Easy' or 'Hard' :  ").lower()
    turns= no_of_terms(difficulty)
    print(f"You have {turns} attempts to guess t e number")
    while not end_check2:
        user= int(input("Make a guess:  "))
        check(number, user)
        cont +=1
        print(f"You have {turns-cont} chances")
        if check(number,user):
            end_check2= True
        if cont == turns:
            print("You lose ☹")
            end_check2=True
    dec= input("Do you want to play Another Game? Y or N   ").lower()
    if dec=='n':
        end_check=True
    else:
        end_check= False
        end_check2= False    
        cont= 0
