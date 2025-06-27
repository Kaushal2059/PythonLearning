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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
user = input("Hello! Enter your name to start up:\n")
user = user.upper()
print(f"HELLO {user} wlecome to Tressure Island.\n Your mission is to find the tressure.")
direction = input("Which way you want to go as left or right:\n")
direction = direction.capitalize()
if direction != "Left":
    print(f"Oops! {user} you fell into a hole.\n Your game is over")
else:
    pond = input("You ended up in a pond.\n Do you want to swim through or wait:\n")
    pond = pond.capitalize()
    if pond == "Swim":
        print("You are attacked by a trout.\n Your game is over")
    elif pond != "Swim" and pond != "Wait":
        print("Your input is invlid please enter eather wait or swim")
    else:
        print("Great for choosing to stay the boat came and took you to" \
        " an island there are three doors you choose one")
        door = input("which door do you want to open. Choose between "\
                     "Red, Blue or Yellow:\n")
        door = door.capitalize()
        if door == "Red": 
            print("Opps! you are burned by fire.\n Better luck next time")
        elif door == "Blue":
            print("You are eaten by beasts.\n Better luck next time")
        elif door == "Yellow":
            print(f"Congrats {user}! You win. Its party time")
        else:
            print("The door you choose doesnot exist.\n your game is over!")



