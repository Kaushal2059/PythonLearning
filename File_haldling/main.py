# file = open("demo.txt", "r") # To open a folder
# contents = file.read() # to read the contents of the file
# print(contents)
# file.close() #Must close a file once it is opened. 

# Another way of doing things so we dont have to manually close a file
# with open ("demo.txt") as file:
#     contents = file.read()
#     print(contents)

# TO write on the file (w => write) If no file exists, w mode will create a file for you0
with open ("C:/Users/rupak/OneDrive/Desktop/demo.txt", mode = "a") as filewrite: # Using absolute path
    filewrite.write(" new file new")

# #To add conent (a => append)
# with open ("demo.txt", mode = "a") as filewrite:
#     filewrite.write(" This is a additional content.")
