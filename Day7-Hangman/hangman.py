import random 
from hangman_art import stages
from hangman_art import logo
from hangman_word import word_list

# word_list=["ardvark","baboon","camel"]
# #word_index= rand.randint(0,len(word_list)-1)
# #word= word_list[word_index]
# display=[]

# lives = len(stages)

# word= rand.choice(word_list).lower()
# for _ in word:
#     display += "_"
# first_letter = input("Enter your 1st letter: " ).lower()


# # for i in range(0, len(word)):
# #     if(word[i] == first_letter):
# #         print("Right")
# #     else:
# #         print("Wrong")
# c = false
# while c != len(word) or lives == 0:
    
#     first_letter = input("Enter your 1st letter: " ).lower()
#     for i in range(len(word)):
#         if(word[i] == first_letter):
#             display[i]= first_letter.upper()    
#         if first_letter not in word:
#             lives -=1
#     print(display)
#     print(stages[lives])
#     c+=1

# if(c== len(word)):
#     print("You Won ")
# else:
#     print("You Lose")

print(logo)

end_of_game = False
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6


print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter.upper()

    

    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        print("""" 
        _
       /(|
      (  :
     __\  \  _____
   (____)  `|
  (____)|   |
   (____).__|
    (___)__.|_____""""")
        break

   
    print(stages[lives])