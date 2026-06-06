# # FileNotFound
# try:
#     file = open("Handling_exception/file.txt") 
#     dict = {"key":"value"}
#     print(dict["key"])

# except FileNotFoundError:
#     open("Handling_exception/file.txt","w")
# except KeyError as error_message:
#     print(f"The key {error_message} doesnot exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file is closed.")
#     raise TypeError("This is an error made by me. Nothing wrong in the code HAAHAHAHAHAHA")

# BMI type error
height = float(input("Enter your height in feet: "))
weight = float(input("Enter your weight in kg: "))

if height > 10:
    raise ValueError("Human height cannot be over 10 feet.")
elif weight > 800:
    raise ValueError("Human weight cannot be over 800 kilos")

bmi = weight / height ** 2
print(f"your bmi is {bmi}")
       







# IndexError
# friuits = ["apple", "banana", "orange"]
# friuit = friuits[4]

# TypeError
# text = "abcc"
# print(text+5)
