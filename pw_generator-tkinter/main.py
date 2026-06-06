from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()
    new_data  = {website: {
        "email":email,
        "password":password
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="error", message="No fields should be empty!")
    else:
        try:
            with open("pw_generator-tkinter/data.json", mode = "r") as file:
                # read the old data
                data = json.load(file)          
        except FileNotFoundError:
            with open("pw_generator-tkinter/data.json", mode = "w") as file:
                # save the updated data
                json.dump(new_data, file, indent = 4)
        else:
             #update the old data with the new one
            data.update(new_data)
            with open("pw_generator-tkinter/data.json", mode = "w") as file:
                #saving the old data
                json.dump(data, file, indent = 4)
        finally:
            website_field.delete(0,END)
            password_field.delete(0,END)

def search():
    search.

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")  
window.config(padx=50, pady= 50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="pw_generator-tkinter/logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(row=0, column=1)

#labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text= "Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)


# fields
website_field = Entry(width=17)
website_field.grid(row= 1, column= 1)
website_field.focus()
email_field = Entry(width=35)
email_field.grid(row= 2, column= 1, columnspan=2)
email_field.insert(0,"demo@gmail.com")
password_field = Entry(width=17)
password_field.grid(row= 3, column= 1)

#buttons
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3, column=2)
search = Button(text="search", command=search)
search.grid(row= 1, column=2 )
add = Button(text="Add", width=30, command=save)
add.grid(row=4, column=1, columnspan=2)









window.mainloop()