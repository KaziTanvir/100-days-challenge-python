import random as ran
user=int(input("What do you want to choose? 0 for rock, 1 for paper and 2 for scissors \n"))

computer= ran.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
table=[rock,paper,scissors]

print(f"{table[user]}\n")
print(f"Computer Chose: \n {table[computer]}")

if user >= 3 or user < 0: 
  print("You typed an invalid number, you lose!") 
elif user == 0 and computer == 2:
  print("You win!")
elif computer == 0 and user == 2:
  print("You lose")
elif computer > user:
  print("You lose")
elif user > computer:
  print("You win!")
elif computer == user:
  print("It's a draw")


    
