from tkinter import *
import os
import sys
import requests
API_ENDPOINT = "https://api.kanye.rest"

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

background_path = resource_path("./kanye-quotes-start/background.png")
kanye_path = resource_path("./kanye-quotes-start/kanye.png")

first_response = requests.get(url=API_ENDPOINT, timeout=10)
first_response.raise_for_status()
first_data = first_response.json()

def get_quote():
    response = requests.get(url=API_ENDPOINT, timeout=10)
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=background_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=first_data["quote"], width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye_path)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()