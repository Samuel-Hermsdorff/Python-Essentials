from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import sys
import os

FONT = ("Arial", 10, "bold")

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image_path = resource_path("logo.png")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)  

    password = "".join(password_list)
    pass_entry.delete(0, last=END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("./data.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(message="No detail for the website exists")
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save user inputs into a file called data.txt: Site | email | password
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("./data.json", "r",  encoding='utf-8') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w", encoding="utf-8") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("./data.json", "w", encoding='utf-8') as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:        
            website_entry.delete(0, last=END)
            pass_entry.delete(0, last=END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=45)

# Canvas - logo image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Label - Website
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

# Label - Email/Username
email_username_label = Label(text="Email/Username:", font=FONT, padx=10)
email_username_label.grid(column=0, row=2)

# Label - Password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

# Entry - Website
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

# Entry - Email/Username
email_entry = Entry(width=50)
email_entry.insert(0, "samuelhermsdorff@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="we")

# Entry - Password
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky="w")

# Button - Generate Password
generate_pass_label = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_label.grid(column=2, row=3)

# Button - Add
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="we")

# Button - Search
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()