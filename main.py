from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, sticky="ew")

website_label = Label(text="Website:", font=("Arial", 14, "bold"))
website_label.grid(column=0, row=1, sticky="w")

email_label = Label(text="Email/Username:", font=("Arial", 14, "bold"))
email_label.grid(column=0, row=2, sticky="w")

password_label = Label(text="Password:", font=("Arial", 14, "bold"))
password_label.grid(column=0, row=3, sticky="w")

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", highlightthickness=0)
generate_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", highlightthickness=0, width=33)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
