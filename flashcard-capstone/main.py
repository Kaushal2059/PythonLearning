from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
new_data = {}

try:
    data = pandas.read_csv("flashcard-capstone/data/words_to_learn.csv")
except FileNotFoundError:
    original_data =  pandas.read_csv("flashcard-capstone/data/french_words.csv")
    new_data = original_data.to_dict(orient="records")
else:
    new_data = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_data)
    new_french_word = current_card["French"]
    canvas.itemconfig(title, text = "French", fill = "black")
    canvas.itemconfig(word, text = new_french_word, fill = "black")
    canvas.itemconfig(image, image= card_front)
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(image, image= card_back)
    canvas.itemconfig(title, text = "English", fill = "white")
    canvas.itemconfig(word, text = english_word, fill = "white")

def is_known():
    new_data.remove(current_card)
    learned_list = pandas.DataFrame(new_data)
    learned_list.to_csv("flashcard-capstone/data/words_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Flashy")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas =Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="flashcard-capstone/images/card_front.png")
card_back = PhotoImage(file="flashcard-capstone/images/card_back.png")
image = canvas.create_image(400, 260, image = card_front)
title = canvas.create_text(400, 200, font=("courier", 30, "italic"))
word = canvas.create_text(400, 300, font=("courier", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="flashcard-capstone/images/wrong.png")
cross_button = Button(image=cross, highlightthickness=0, command = next_card)
cross_button.grid(row=1, column=0)

tick = PhotoImage(file="flashcard-capstone/images/right.png")
right_button = Button(image=tick, highlightthickness=0, command = is_known)
right_button.grid(row= 1, column=1 )

next_card()
window.mainloop()
