from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made false if ingredients are not sufecient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns total from the coins inserterd"""
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickels?:")) * 0.05
    total += int(input("how many pennis?:")) * 0.01
    return total


def is_transaction_sucessul(money_received, drink_cost):
    """Returns True if payment is accepted and False if money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit =+ drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingrediets):
    for item in order_ingrediets:
        resources[item] -= order_ingrediets[item]
    print(f"Here is your {drink_name} ☕. Enjoy your coffee and dont forget to visit us again.😀")


is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input  == "report":
       print(f"water: {resources['water']}")
       print(f"milk: {resources['milk']}")
       print(f"coffee: {resources['milk']}")
       print(f"money: {resources['money']}")
    else:
        drink = MENU[user_input]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessul(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
