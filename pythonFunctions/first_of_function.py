def new_function():  # def defines the name of the function and paranthesis differs functions from a variable name. and : denotes anything after it is a part of that function followed by indentation
    print("hello")
    print("Bye")

new_function()  # this way you can call the function
    
def practice():
    print("Hello world")
    print("Hello world")
    print("Hello world")

practice()

# Functoin that allows for input as a parameter

def greet(name):
    print(f"Hello {name}")
    print("How do you do")

greet("kaushal")  # Here name is referred as the parameter and kaushal is the argument

# function with more than one parameter with positional arguments
def two_parameters_function(name,age):
    print(f"Hello I am {name} and I am {age} years old")
    
two_parameters_function("ram","twnety")

# function with more than one parameter with keyword arguments
def two_parameters_function2(name,age):
    print(f"Hello I am {name} and I am {age} years old")
    
two_parameters_function2( age = "twnety", name = "ram")