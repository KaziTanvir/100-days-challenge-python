from itertools import count
from game_data import data
import art 
import random as rand

def get_account():
    return rand.choice(data)

def print_info(c_guess):
    name= c_guess["name"]
    description = c_guess["description"]
    country = c_guess["country"]
    
    return f"{name}, a {description}, from {country}"

def game_check(guess, a,b):
    if a>b :
        return guess== "a"
    else:
        return guess == "b"
    
end_check= False
print(art.logo)
a= get_account()
b=get_account()
score=0
while not end_check:
    a=b
    b=get_account()
    while a == b:
        b= get_account()
    
    print(f"Compare A: {print_info(a)}")
    print(art.vs)
    print(f"Against B : {print_info(b)}")
    
    guess= input("Who has more follower? Type A or B:  ").lower()
    a_count= a["follower_count"]
    b_count = b["follower_count"]
    check= game_check(guess, a_count,b_count)
    
    if check:
        score +=1
        print(f"you are right with a score of {score}")
    else:
        end_check=True
        print(f"Sorry you lose. Score : {score}")
        
    
