############### Blackjack Project #####################
import random
from blackjack_art import logo
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   return cards[random.choice(cards)]


def calculate_score(list_cards):
   if sum(list_cards) == 21 and len(list_cards) == 2:
      return 0
   if 11 in list_cards and sum(list_cards) > 21:
       list_cards.remove(11)
       list_cards.append(1)
   return sum(list_cards)

def compare(user_score , computer_score):
   if computer_score == user_score:
      return("Draw match")
   elif computer_score == 0:
      return("You loss .  Opponent has Blackjack")
   elif user_score == 0:
      return("You got Blackjack . You won")
   elif user_score >21:
      return("You went over . You loss")
   elif computer_score >21:
      return ("opponent went over . You Win")
   elif user_score > computer_score:
      return ("You Win")
   else:
      return "You Loss"
def playgame():
   print(logo)
   user_cards = []
   computer_cards = []
   end_game = False
   for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
   while not end_game:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)

      print(f"You cards are  {user_cards} and score is {user_score}")
      print(f"Computer first card is {computer_cards[0]} ")

      if user_score == 0 or computer_score == 0 or user_score > 21 :
         end_game = True
      else:
         user_should_deal = input("If you want to draw another card type 'y' or type 'n' to pass : ")
         if user_should_deal == "y":
            user_cards.append(deal_card())
         else:
            end_game = True

   while computer_score != 0 and computer_score <= 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)


   print(f"You final hand is  {user_cards} and score is {user_score}")
   print(f"Computer final hand is {computer_cards} and score is {computer_score}")
   print(compare(user_score , computer_score))

while input("Do you want to play Blackjack , type 'y' or 'n' : ") == "y":
   playgame()