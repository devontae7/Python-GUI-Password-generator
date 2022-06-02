from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip  # this module copy text automaticaly. we use it for generated pass to copy
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
               '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    # passs = ''
    # for char in password_list:
    #     passs += char
    passs = "".join(password_list)
    p_feild.delete(0, END)
    p_feild.insert(0, passs)


def find_password():
    search_text = web_feild.get()
    try:
        with open("data.json", "r") as data:
            text = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message="No data found")
        # for i in text:
        #         if search_text == i:
        #             messagebox.showinfo(title="Details", message=f"Email: {text[search_text]['email']} \n"
        #                                                      f"Password: {text[search_text]['password']}")
        #         else:
        #             messagebox.showinfo(title="Opps", message="No data found")
    else:
        if search_text in text:
            messagebox.showinfo(title="Details", message=f"Email: {text[search_text]['email']} \n"
                                                         f"Password: {text[search_text]['password']}")
        else:
            messagebox.showinfo(title="Opps", message=f"No Entry for website: {search_text}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = web_feild.get()
    email = e_feild.get()
    password = p_feild.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oppss", message="Please do not leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading json data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # updating old data with new data
        else:
            data.update(new_data)
            with open("data.json", "w") as data_files:
                # write data
                json.dump(data, data_files, indent=4)
        finally:
            web_feild.delete(0, END)
            p_feild.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass")
# window.minsize(width=400,height=400)
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_lb = Label(text="Website:")
web_lb.grid(column=0, row=1)

user_lb = Label(text="Email/UserName:")
user_lb.grid(column=0, row=2)

pass_lb = Label(text="Pasword:")
pass_lb.grid(column=0, row=3)

web_feild = Entry(width=40)
web_feild.grid(column=1, row=1)
web_feild.focus()

e_feild = Entry(width=40)
e_feild.grid(column=1, row=2)
e_feild.insert(0, "habib.rehman0088@gmail.com")

p_feild = Entry(width=40)
p_feild.grid(column=1, row=3)

bt = Button(text="Generate Password", command=generate_password)
bt.grid(row=3, column=2)

add_bt = Button(text="Add", width=34, command=add_data)
add_bt.grid(column=1, row=4)

search_bt = Button(text="Search", width=15, command=find_password)
search_bt.grid(column=2, row=1)

window.mainloop()
