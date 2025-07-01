import string
import random 

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

username = input("Enter your username to continue:\n").upper()
print(f"HELLO {username}! welcome to the random password generator")

no_of_letters = int(input("Enter the number of letters you want in your password:\n"))
no_of_symbos = int(input("Enter the number of symbols you want in your password:\n"))
no_of_numbers = int(input("Enter the number of numbers you want in your password:\n"))

random_characters = random.sample(letters, no_of_letters)
random_symbols = random.sample(symbols, no_of_symbos)
random_numbers = random.sample(numbers, no_of_numbers)

your_password = random_characters+random_symbols+random_numbers
random.shuffle(your_password) #random.suffle modifies the list and use it directly. No need to store in seperate variable
password_in_string = "".join(your_password)

print(f"The final password for user {username} is {password_in_string}")