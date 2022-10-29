print("Welcome to Pizza Order.")
size= (input("What is the size of your pizza ? S , M , L ?"))
add_pepperoni= (input("Do you want to add extra pepperoni ? Y , N ?"))
extra_cheez= (input("Do you want to add extra cheez ? Y , N ?"))
bill = 0

if (size=="S"):
    bill += 15
elif (size=="M"):
    bill += 20
else:
    bill += 25

if size=="S":
    if add_pepperoni == "Y":
        bill += 2
else:
    bill+=3
if extra_cheez == "Y":
    bill += 1

print(f"Your total bill is ${bill}")