from os import system
from art import calc

print(calc)

def addition(first, second):
    """ Takes two number and prints the sum"""
    return first + second


def subtraction(first, second):
    """ Takes two number and prints the difference"""
    return first - second

def multiplicaton(first, second):
    """ Takes two number and prints the product"""
    return first * second
    
def division(first, second):
    """ Takes two number and prints the division"""
    return first / second

dict_of_operands = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplicaton,
    "/" : division
}

is_continue = True
first_number = float(input("Enter the first number:\n"))
while is_continue:
    for symbols in dict_of_operands:
        print(symbols)
    operand = input("Choose the operation you want to perform:\n")
    second_number = float(input("Enter the second number:\n"))
    result = (dict_of_operands[operand](first_number,second_number))
    print(f"{first_number} {operand} {second_number} = {result}")
    
    goon = input(f"Type 'y' to continue calculaing with {result}, or type 'n' to start a new calculation or 'quit' to stop calculator:\n").lower()
    
    if goon == "y":
        first_number = int(result)
        print("\n" * 3)
    elif goon == "n":
        system("cls")
        print(calc)
        first_number = float(input("Enter a new first number:\n"))
    elif goon == "quit":
        is_continue = False
        print("Thank you for using my calculator")        
    else:
        print("only 'y','n'")        
