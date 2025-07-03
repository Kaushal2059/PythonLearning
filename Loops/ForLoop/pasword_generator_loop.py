import string
import random 

letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

username = input("Enter your username to continue:\n").upper()
print(f"HELLO {username}! welcome to the random password generator")

no_of_letters = int(input("Enter the number of letters you want in your password:\n"))
no_of_symbos = int(input("Enter the number of symbols you want in your password:\n"))
no_of_numbers = int(input("Enter the number of numbers you want in your password:\n"))

password = ""
for char in range(0, no_of_letters):
    password += random.choice(letters)
for char in range(0, no_of_symbos):
    password += random.choice(symbols)
for char in range(0, no_of_numbers):
    password += random.choice(numbers)

# print(password)

# using list 
password_list = []
for char in range(0, no_of_letters):
    password_list.append(random.choice(letters))
for char in range(0, no_of_symbos):
    password_list.append(random.choice(symbols))
for char in range(0, no_of_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# final_password = "".join(password_list)

final_password = ""
for char in password_list:
    final_password += char

print(final_password)