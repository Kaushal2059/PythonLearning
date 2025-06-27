print("Greetings! welcome to the pizza delivery app")
size = input("Enter the size of pizza that you want. s for small m for medium l for large:\n")
price = 0
Pepperoni = input("Do you want to add pepperoni to your pizza. say y for yes and n for no:\n")
extra_cheese = input("Do you want extra cheese in your pizza. Say y for yes and n for no:\n")
if size == "s":
    price += 15
elif size == "m":
    price += 20
elif size == "l":
    price += 25
else :
    print("Ooops, invalid input! Please type s, m or l")

if Pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "y":
    price += 1

print(f"your final prie of the pizza is ${price}")