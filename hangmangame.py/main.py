import random
from hangma_words import word_list
import hangman_Art


print (hangman_Art.hangmanstart)
print("Hello gamer! welcome to the hangman game")

# difining lives to 6 in the begining of the game

lives = 6

# choosing a word randomly

chosen_word = random.choice(word_list)   

# getting a plceholder to display to the user about the length of the word

placeholder = ""
for position in range (0,len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:

    print(f"********** You have {lives}/6 lives left ********** ")
    guess = input("Guess a letter for the randomly generated word:\n").lower()

    if guess in correct_letters:
        print(f"The letter {guess} is alredy entered")

# Adding letters assigned by the user to the placeholder

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        print(f" The letter {guess} is not in the word.\n You loose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"********** It was {chosen_word}! You lost **********")
    print(display) 

    if "_" not in display:
        game_over = True
        print("********** You Win **********")

    print(hangman_Art.HANGMANPICS[lives])