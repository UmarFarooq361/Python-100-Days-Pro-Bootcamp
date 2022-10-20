import random

names = input(print("Enter everybody names seperated by comma : "))
names = names.split(", ")
nameLength = len(names)
print(nameLength)
random_number = random.randint(0 , nameLength-1)
print(random_number)
print(f"{names[random_number]} is going to pay bills. ")