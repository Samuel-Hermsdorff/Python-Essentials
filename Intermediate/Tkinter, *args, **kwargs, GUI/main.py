from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=20)

#Label
my_label = Label(text="is equal to", font=("Arial", 15, "bold"))
# my_label.config(text="New text")
my_label.grid(column=0, row=1)
# my_label.config(padx=100, pady=20)
# my_label["text"] = "New text"

#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="Click me 2")
new_button.grid(column=2, row=0)
#Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()