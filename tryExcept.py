try:
    age = int(input("Enter your age:\n"))
except ValueError:
    print("you entered an invalid number. Please try again with an numerical value such as '15'. ")
    age = int(input("Enter your age:\n"))

if age > 18:
    print("You are eligible for voting")
else:
    print(f"you can't vote at {age}")