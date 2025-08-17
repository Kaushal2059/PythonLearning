class User:
    def __init__(self, user_id, username): # Creating a starting value for the attributes and it gets triggered everytime you use a class to create an object 
        self.id = user_id
        self.username = username
        self.followers = 0 # Setting a default value  
        self.following= 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("50", "kaushal") # This is a  Constructor
user_2 = User("01", "Virat")

user_1.follow(user_2)

print(user_1.id)
print(user_1.username)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)