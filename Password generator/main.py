from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENEATOR ------------------------------- #

def generate_password():

    '''Generates a random password'''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))] + \
                    [random.choice(numbers) for char in range(random.randint(2, 4))] + \
                    [random.choice(symbols) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, string=password)

    pyperclip.copy(password)    #gets the generated password into the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    ''' Saves the inputs into a file '''

    global DATA_FILE

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 and len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields.")
    elif len(website) == 0:
        messagebox.showerror(title="Error", message="Please, fill in the website.")
    elif len(password) == 0:
        messagebox.showerror(title="Error", message="Please, fill in the password.")
    elif len(email) == 0:
        messagebox.showerror(title="Error", message="Please, fill in the email/username.")
    else:
        add_info = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if add_info == True:
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }


            try:
                with open(DATA_FILE, "r") as data_file:
                    data = json.load(data_file) #Reading old data

            except FileNotFoundError:
                with open(DATA_FILE, "w") as data_file:
                    json.dump(new_data, data_file)

            else:
                data.update(new_data) #Updating old data with new data
                with open(DATA_FILE, "w") as data_file:
                    json.dump(data, data_file, indent=4) # Saving updated data

            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ------------------------- FIND PASSWORDS ---------------------------- #

def find_password():

    '''Searches for the reqeusted password'''

    global DATA_FILE

    try:
        with open(DATA_FILE, "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

    else:
        website = entry_website.get()
        
        if website in data.keys():
            messagebox.showinfo(title=f"{website}", message=f"E-mail/Username: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message="Website not found.")


# ---------------------------- UI SETUP ------------------------------- #

WHITE = "#FFFFFF"
DATA_FILE = "data.json"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#website label
label_website = Label(text="Website:", bg=WHITE)
label_website.grid(row=1, column =0)

#website entry
entry_website = Entry(width=32)
entry_website.grid(row=1, column=1)
entry_website.focus()

#email/user label
label_email = Label(text="Email/Username:", bg=WHITE)
label_email.grid(row=2, column=0)

#email/user entry
entry_email = Entry(width=50)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "izitao@email.com")

#password label
label_password = Label(text="Password:", bg=WHITE)
label_password.grid(row=3, column=0)

#password entry
entry_password = Entry(width=32)
entry_password.grid(row=3, column=1)

#password generator button
button_generate_pw = Button(text="Generate Password", bg=WHITE, command=generate_password)
button_generate_pw.grid(row=3, column=2)

#add button
button_add = Button(text="Add", bg=WHITE, width=43, command=save)
button_add.grid(row=4, column=1, columnspan=2)

#search button
button_search = Button(text="Search", bg=WHITE, width=14, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
