import random
from Art import logo
from os import system

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_sum):
    """calculates the sum of the cards"""
    if sum(card_sum) == 21 and len(card_sum) == 2:
        return 0
    
    if sum(card_sum) > 21 and 11 in card_sum:
        card_sum.remove(11)
        card_sum.append(1)

    return sum(card_sum)

def compare(usr_score, cs_score):
    if cs_score == usr_score:
        return "It's a draw."
    elif cs_score == 0:
        return "The computer has a blackjack. You lost."
    elif usr_score == 0:
        return "CONGRATULATIONS! YOU WON. You have a blackjack."
    elif usr_score > 21:
        return "Your score is greater than 21. You lost."
    elif cs_score > 21:
        return "CONGRATULATIONS! YOU WON. The computer has a score of more than 21."
    elif usr_score > cs_score:
        return "CONGRATULATIONS! YOU WON. Your score is more than computer."
    else:
        return ("Computer score is more than yours. You lost.")

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    for _ in range(2):
        # new_card = deal_card()
        user_cards.append(deal_card()) # when you want to add a single item on the list not the list than you need to use apped
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}.\n Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card 'n' to pass:\n").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score =calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game of blackjack. Type 'y' or 'n':\n").lower() == "y":
    system("cls")
    play_game()