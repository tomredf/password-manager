from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    website = website_entry.get()

    if len(website) > 0:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo("Search Failed", "There are no saved passwords")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo("Search Failed", f"{website} not found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Missing Website", message=f"Please enter a website")
        return

    if len(email) == 0:
        messagebox.showinfo(title="Missing Email/Username", message=f"Please enter an email or username")
        return

    if len(password) == 0:
        messagebox.showinfo(title="Missing Password", message=f"Please enter a password")
        return

    result = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIs this ok to save?")

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if result:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(END, "test123@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", highlightthickness=0, width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

search_button = Button(text="Search", highlightthickness=0, command=search)
search_button.grid(column=2, row=1, sticky="ew")

window.mainloop()
