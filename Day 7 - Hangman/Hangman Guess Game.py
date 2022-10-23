import random
word_list = ["mouse" , "keyboard" , "monitor"]

chosen_word = random.choice(word_list )
display = []
for push in chosen_word:
    display.append("_")
print(display)
guess = input("Guess the letter : ").lower()
for position in range(len(chosen_word)):
    check = chosen_word[position]
    if check == guess:
        display[position] = guess
    # else:
    #     print("wrong")
print(display)
print(chosen_word)