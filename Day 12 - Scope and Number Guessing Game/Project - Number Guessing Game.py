import random
from art import logo
print(logo)
print("Welcome to Numebr Guessing Game!")
print("I am thinking of number between 1 to 100 .")
no_of_guess = 0
random_number = random.randint(0 , 100)
level = input("Choose difficulty level . Type 'hard' or 'easy' : ").lower()
if level == "hard":
    no_of_guess = 5
elif level == "easy":
    no_of_guess = 10

while no_of_guess > 0:
    print(f"You have {no_of_guess} remaining attempts to guess the number.")
    guess_number = int(input("Make a guess : "))
    if guess_number > random_number:
        print("Too High . Guess Again")
    elif guess_number < random_number:
        print("Too low . Guess Again")
    else:
        print("You have made a right guess . Congrats")
        break
    no_of_guess -= 1
    if no_of_guess == 0:
        print("You have run out of guesses . You loss")



