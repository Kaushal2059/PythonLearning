import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playgame = True
while playgame:
    game = input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n").lower()
    if game == 'y':

        computer_choice = random.sample(cards, 2)
        sum_of_computer_choice = 0
        for choice in computer_choice:
            sum_of_computer_choice += choice

        userChoice = random.sample(cards, 2)
        sum_of_initial_cards_choosen = int(sum(userChoice))
        for cardsss in userChoice:
            cards.remove(cardsss)    
        if sum_of_initial_cards_choosen > 21:
            print(f"You loose your score is {sum_of_initial_cards_choosen}")

        print(f"Your cards: {userChoice}, current score: {sum_of_initial_cards_choosen}")
        print(f"Computer's first card: {computer_choice[0]}")

        if sum_of_initial_cards_choosen < 17:
            print("You must take another card")
            
        else:
            pick_a_card = input("Do you want to pick another card. Type 'y' or 'n':\n")
            if pick_a_card == 'y':
                print("To be continuued")
            elif pick_a_card == 'n':
                print("To be continued 3")

    elif game == 'n':
        playgame = False
        print("SEE YOU AGAIN!")
