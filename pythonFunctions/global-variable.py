variable = 1
PI = 3.14159 # GLOBAL COSTANTS GENERALLY DENOTED BY UPPER CASE CHARACTERS

def new_fuction(new_variable):
    # global variable # takes the global function variable into the function but its not a good practice to modify the global scope
    return new_variable + 1

modified_variable = new_fuction(variable)
print(modified_variable)