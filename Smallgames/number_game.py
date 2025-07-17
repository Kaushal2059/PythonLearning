import random

print("Welcome to the number guessing gmae!:\n I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty between 'easy' and 'hard':\n").lower()
CHOICE = random.randint(1, 100)

def game(a):
    global CHOICE
    for chance in range(a, 0, -1 ):
        print(f"you have {chance} attempts remaining to guess the number")
        new_input = int(input("Make a guess: "))
        if new_input == CHOICE:
            print("congratulatios you entered a correct number")
            break
        elif new_input > CHOICE:
            print("Too high")
        elif new_input < CHOICE:
            print("Too low")
    else:
        print(f"GAME OVER! You didn't choose a correct answer. The correct answer is {CHOICE}")

if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)

