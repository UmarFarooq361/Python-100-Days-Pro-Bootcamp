import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = int(input(print("What do you choose ? Type 0 for Rock , 1 for Paper , 2 for Scissor ")))
computer_choice = random.randint(0,2)
if player_choice >= 3 or player_choice < 0:
    print("Invalid number .")
else:
  if (player_choice == 0 and computer_choice== 1):
      print(f"You choose {rock}")
      print(f"Computer choose {paper}")
      print(f"Computer Won . You loss")
  elif player_choice == 0 and computer_choice== 2:
    print(f"You choose {rock}")
    print(f"Computer choose {scissor}")
    print("You Won")
  elif (player_choice == 1 and computer_choice== 2):
    print(f"You choose {paper}")
    print(f"Computer choose {scissor}")
    print("Computer Won . You loss")
  elif (player_choice == 1 and computer_choice== 0):
    print(f"You choose {paper}")
    print(f"Computer choose {rock}")
    print("You Won")
  elif player_choice == 2 and computer_choice== 1:
    print(f"You choose {scissor}")
    print(f"Computer choose {paper}")
    print("You Won")
  elif player_choice == 2 and computer_choice== 0:
    print(f"You choose {scissor}")
    print(f"Computer choose {rock}")
    print("Computer Won . You loss")
  else:
    print("Match Draw!")
