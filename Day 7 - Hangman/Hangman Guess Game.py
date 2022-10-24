import random
from hangman_art import logo , stages
from hangman_words import word_list
print(logo)
chosen_word = random.choice(word_list)
chosen_length = len(chosen_word)
display = []
lives = 6

for push in chosen_word:
    display.append("_")
print(display)
end_of_game = False
while not end_of_game :
    if lives == 0:
        print("You are out of lives .\nYou loss.")
        break
    guess = input("Guess the letter : ").lower()
    if guess in display:
        print(f"You already guessed the letter {guess}")
    for position in range(chosen_length):
        check = chosen_word[position]
        if check == guess:
           display[position] = guess

    if guess not in display:
        print(f"You guessed {guess} .Thats not in the word. You lose a life.")
        lives -= 1
        print(f"lives = {lives}")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Won")
    print(stages[lives])
print(chosen_word)