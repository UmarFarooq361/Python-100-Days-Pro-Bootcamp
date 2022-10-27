from auction_art import logo
import os
clear = lambda: os.system('cls')

print(logo)
print("Welcome to the Secret Auction Program")


other_bidder = True
bidder_dictionary = {}

def highest_bidder(bidder):
    max_bid = 0
    winner = ""
    for key in bidder:
        bid_amount = bidder[key]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = key
    print(f'The winner is {winner} with the highest bid of {max_bid}')
while other_bidder:
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    bidder_dictionary[name] = bid
    new_bidder = input("Is there any other bidder ? type 'yes' or 'no' : " )
    if new_bidder == "no":
        other_bidder = False
        highest_bidder(bidder_dictionary)
    else:
        clear()

