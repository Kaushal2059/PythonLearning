# Nested if else
print("Welcome to the rollercoaster ride!")
Height = int(input("enter your heignt in cm:\n"))
ticket = 0


if Height > 120:
    print("Congrats! You can ride the roller coaster")
    Age = int(input("Now enter your age:\n"))
  
    if Age <= 12 :
        ticket = 5   
    elif Age <= 18:
        ticket = 7  

    elif Age >= 45 and Age <= 55:
        print("YOU HAVE A MIDLIFE CRISIS AND YOUR TICKET IS FREE") 

    else:
        ticket = 18  
    value = input(f"DO you want to take photos? Type y yes and n for no. If not your ticket price is ${ticket} if yes it will be increased by $3:\n")
    if value == "y":
        ticket += 3

    print(f"your ticket price is {ticket}")

else:
    print("Sorry! You cant ride the roller coaster")


# check even or oddd
# number = int(input("Enter the number you want to check"))
# if number % 2 == 0:
#     print("The number is even number")
# else:
#     print("The number you entered is odd")


