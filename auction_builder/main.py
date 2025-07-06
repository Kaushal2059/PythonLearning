from ascii import logo
from os import system

print(logo)
print("Welcome to the secret auction program")

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")

dictionary_of_bidders = {}
other_person = True
while other_person:
    name = input("Enter what is your name: ")
    bid_amount = int(input("what is your bid amount? "))
    dictionary_of_bidders[name] = bid_amount
    person_remaining = input("Is there any other person after you? type 'yes' or 'no' ").lower()
    if person_remaining == "no":
        other_person = False
        highest_bidder(dictionary_of_bidders)
    elif person_remaining == "yes":
        system("cls")


