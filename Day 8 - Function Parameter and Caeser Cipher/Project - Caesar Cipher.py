from cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caesar(text , shift , direction):
    converted_text = ""
    for char in text:
        if char in alphabet:
          position = alphabet.index(char)
          if direction == "encode":
            new_position = position + shift
          elif direction == "decode":
            new_position = position - shift
          new_position = new_position % 26
          encrypt_letter = alphabet[new_position]
          converted_text += encrypt_letter
        else:
            converted_text += char
    print(f"The {direction}d text is {converted_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text , shift , direction)
  exit = input("Do you want to continue ? type 'yes' to continue or 'no' to exit : ").lower()
  if exit == "no":
      should_continue = False
      print("Goodbye")

