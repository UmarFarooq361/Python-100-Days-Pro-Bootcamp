from tkinter import *
from tkinter import messagebox
window = Tk()
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    my_username = username_input.get()
    my_password = password_input.get()
    new_data = {
        website_name:{
            "email": my_username,
            "password": my_password
        }
    }
    if len(website_name)== 0 or len(my_username) == 0 or len(my_password) == 0:
        messagebox.showwarning(title="Emply Fields", message="You cant left any field emply.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data , data_file , indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data , data_file , indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website_name = website_input.get()
    if len(website_name)== 0 :
        messagebox.showwarning(title="Emply Fields", message="Type website name to find its password.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                if website_name in data:
                    email = data[website_name]["email"]
                    password = data[website_name]["password"]
                else:
                    messagebox.showwarning(title="Error", message=f"No details for the {website_name} found.")


        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file exists.")

        else:
            messagebox.showinfo(title=website_name, message=f"Email: {email}\n Password: {password}")

        finally:
            website_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height= 200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column=1, row=0)

website = Label(text= "Website", font= ("Ubuntu", 15))
website.grid(column=0, row=1)
website_input = Entry(width= 20 ,font= ("Ubunto", 15))
website_input.focus()
website_input.grid(row=1 , column=1)
search_btn = Button(text= "Search" ,font= ("Ubuntu", 13),width=16, command= find_password )
search_btn.grid(column=2, row=1)

user_name = Label(text= "UserName/Email", font= ("Ubunto", 15))
user_name.grid(column=0, row=2)
username_input = Entry(width= 35 ,font= ("Ubunto", 15) )
username_input.grid(row=2 , column=1, columnspan=2)

password = Label(text= "Password", font= ("Ubunto", 15))
password.grid(column=0, row=3)
password_input = Entry(width= 21 ,font= ("Ubunto", 15) )
password_input.grid(row=3 , column=1)
pass_generate_btn = Button(text= "Generate Password" ,font= ("Ubuntu", 13), command= generate_password )
pass_generate_btn.grid(column=2, row=3)
# pass_generate_btn.config(pady= 1, padx=3 )

add_password_btn = Button(text= "Add Password" ,font= ("Ubuntu", 14), width=35 , command=save)
add_password_btn.grid(column=1, row=4, columnspan=2)
# add_password_btn.config(pady= 1, padx=3 )

window.mainloop()