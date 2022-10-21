#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list  =[]
for let in range( 0 , nr_letters ):
    password_list += letters[random.randint( 0 , len(letters)-1)]

for let in range( 0 , nr_symbols ):
    password_list += symbols[random.randint( 0 , len(symbols)-1)]

for let in range( 0 , nr_numbers ):
    password_list += numbers[random.randint( 0 , len(numbers)-1)]

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your recommended password is {password}")
