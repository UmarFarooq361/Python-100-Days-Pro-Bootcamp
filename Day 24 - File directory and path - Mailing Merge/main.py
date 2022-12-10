placeholder = "[name]"
with open("./Inputs/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Inputs/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter.replace(placeholder , striped_name)
        # print(new_letter)
        with open(f"./Outputs/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)