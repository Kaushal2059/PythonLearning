import random

hangman = '''
 _
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
                    
             '''


HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']



print (hangman)
print("Hello gamer! welcome to the hangman game")

# Providing computer the words to play with
word_list = ["kaushal", "mehool", "biswas", "harihar", "sitaram", "bishnu", "kalpana", "yuvraj"]

lives = 6
# choosing a word randomly
chosen_word = random.choice(word_list)   
print (chosen_word)

# getting a plceholder to display to the user about the length of the word
placeholder = ""
for position in range (0,len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:


    guess = input("Guess a letter for the randomly generated word:\n").lower()

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
        

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost")

    if "_" not in display:
        game_over = True
        print("You Win")
    print(HANGMANPICS[lives])