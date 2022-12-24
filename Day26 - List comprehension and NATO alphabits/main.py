import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
err = True
while err:
    name = input("Enter your name: ").upper()
    try:
        nato_name = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry enter only alphabets please")
    else:
        print(nato_name)
        err = False
