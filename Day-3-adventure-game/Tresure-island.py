print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

LR= input("Where do you want to go Left or Right? ").lower()
if LR == "left":
    print("You have reached a river filled with deadly snakes and crocodiles \n")
    SW= input("Do you want to wait for the boat or swim across?  Wait or Swim   ").lower()
    if SW=="wait":
        print("You have reached the final step \n There are 3 doors. 2 doors lead to your death !!")
        door= input("Which door do you pick? Red, yellow or green ").lower()
        if door == "yellow":
            print("Congratulations!!!! Here is your Legendary treasure of the 40 kings!!!")
        else:
            print("You met Thanos, he used the mind stone to turn you into dust")
    else:
        print("Are you mad or what!!!!!!!! Enjoy death!!!!!!!!!!")
else:
    print("Use your brain Idiot!!!!!!! Saw right and went right!!! Baka!!!!!!!!!!")