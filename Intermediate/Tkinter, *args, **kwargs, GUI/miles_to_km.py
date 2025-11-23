from tkinter import *

def button_clicked():
    km = float(user_input.get()) * 1.609
    num_label.config(text=km)

#Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Label - equal
eq_label = Label(text="is equal to", font=("Arial", 10, "bold"))
eq_label.grid(column=0, row=1)

#Label - miles
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

#Label - km
km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

#Label - number
num_label = Label(text="0", font=("Arial", 10, "bold"))
num_label.grid(column=1, row=1)

#Entry
user_input = Entry(width=12)
user_input.grid(column=1, row=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)







window.mainloop()