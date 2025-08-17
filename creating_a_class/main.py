class User:
    def __init__(self, user_id, username): # Creating a starting value for the attributes and it gets triggered everytime you use a class to create an object 
        self.id = user_id
        self.username = username
        self.followers = 0 # Setting a default value                      

#  Creating a  object using a class
user_1 = User("50","kaushal") # This is a  Constructor

# creting an attribute using object (attribute is a variable that is associated with an object)
# user_1.id = 50
# user_1.username = "Kaushal"

print(user_1.id)
print(user_1.username)



