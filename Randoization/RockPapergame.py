import random
print("welcome to the rock paper sizzor game")

input_value = int(input("Enter what you want to choose? Enter 0 for rock 1 for paper and 2 for sissor"))

computer_choice = random.randint(0,2)
print(f"The computer choose {computer_choice}")

if input_value == 0 and computer_choice == 2:
    print("congratulations you won! ")
elif computer_choice == 0 and input_value == 2:
    print("Opps! you lost against the computer.")
elif input_value > computer_choice:
    print("congratulations you won!")
elif computer_choice > input_value:
    print("Opps! you lost against the computer.")
elif computer_choice == input_value:
    print("Its a draw. Try again for the reasult hopefully")
else:
    print("You typed an invalid number. You losed!")
    