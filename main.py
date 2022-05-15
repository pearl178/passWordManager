from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_chosen = [choice(letters) for _ in range(0, randint(8, 10))]
    symbols_chosen = [choice(symbols) for _ in range(0, randint(2, 4))]
    numbers_chosen = [choice(numbers) for _ in range(0, randint(2, 4))]
    password = letters_chosen + symbols_chosen + numbers_chosen
    shuffle(password)
    password_random = "".join(password)
    password_input.insert(0, password_random)
    pyperclip.copy(password_random)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any field empty")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername:{username}"
                                                  f"\nPassword{password}\nIs this OK to save?")

        if is_ok:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(message="Please enter a website first")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                if website in data:
                    messagebox.showinfo(title=website, message=f"Username:\n{data[website]['username']}"
                                                               f"\nPassword:\n{data[website]['password']}")
                else:
                    messagebox.showinfo(message="No details for the website exists.")
        except FileNotFoundError:
            messagebox.showinfo(message="No data file found.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Management")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

website_input = Entry(width=35)
website_input.grid(column=1, row=2)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=3)

username_input = Entry(width=35)
username_input.grid(column=1, row=3, columnspan=2)
username_input.insert(0, "pearlsai91@gmail.com")

password_label = Label(width=21, text="Password:")
password_label.grid(column=0, row=4)

password_input = Entry(width=21)
password_input.grid(column=1, row=4)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=4)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text='Search', command=search_password, width=13)
search_button.grid(column=2, row=2)


window.mainloop()
