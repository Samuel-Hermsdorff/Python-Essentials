from tkinter import *
from tkinter import messagebox
import json
import pandas as pd
import random as rd
import csv
import os
import sys

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_COLOR = "#FFFFFF"
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

card_back_path = resource_path("./images/card_back.png")
card_front_path = resource_path("./images/card_front.png")
right_path = resource_path("./images/right.png")
wrong_path = resource_path("./images/wrong.png")
french_words_path = resource_path("./data/french_words.csv")
words_to_learn_path = resource_path("./data/words_to_learn.csv")

current_card = {}
words_dict = {}

try:
    data = pd.read_csv(words_to_learn_path)
except FileNotFoundError:
    original_data = pd.read_csv(french_words_path)
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")

# Take words function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(words_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    print(current_card)    
    flip_timer = window.after(3000, flip_card)
# If user knows the word 
def word_learned():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv(words_to_learn_path, index=False)
    next_card()
# Show back card
def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# Create user interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    # front card image
card_front_image = PhotoImage(file=card_front_path)
card_back_image = PhotoImage(file=card_back_path)
card_image = canvas.create_image(400,263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Known button
check_image = PhotoImage(file=right_path)
known_button = Button(image=check_image, highlightthickness=0, command=word_learned)
known_button.grid(column=1, row=1)

# Unknown button
cross_image = PhotoImage(file=wrong_path)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Language Label
language_label = Label(text="French", font=("Arial", 60, "bold"), bg=FRONT_CARD_COLOR, highlightthickness=0)

# Word Label
word_label = Label(text="word", font=("Arial", 60, "bold"), bg=FRONT_CARD_COLOR, highlightthickness=0)

next_card()





window.mainloop()