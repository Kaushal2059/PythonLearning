import random
hangman = """
 _
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
                    
             """

print (hangman)
print("Hello gamer! welcome to the hangman game")

# Providing computer the words to play with
word_list = ["kaushal", "mehool", "biswas", "harihar", "sitaram", "bishnu", "kalpana", "yuvraj"]

# choosing a word randomly
for chosen_word in range(0,len(word_list)):
    chosen_word = random.choice(word_list)
   
print (chosen_word)

# getting a plceholder to display to the user about the length of the word
placeholder = ""
for position in range (0,len(chosen_word)):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter for the randomly generated word:\n").lower()

# Adding letters assigned by the user to the placeholder
display = ""
for letter in range(0, len(chosen_word)):
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
print(display)


