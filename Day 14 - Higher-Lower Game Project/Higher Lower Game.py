import random
from art import logo , vs
from game_data import data
print(logo)

score = 0
game_continue = True

def more_follower(choose , A_followers , B_followers):
    if A_followers > B_followers:
        return choose == "a"
    else:
        return choose == "b"

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f' {name}, a {description}, from {country}')

B = random.choice(data)
while game_continue:
    A = B
    B = random.choice(data)
    while A == B:
        B = random.choice(data)
    print(f'Compare A : {format_data(A)}')
    print(vs)
    print(f'Against B : {format_data(B)}')

    choose = input("Who has more instagram followers. Type 'A' or 'B' : ").lower()
    is_correct = more_follower(choose , A["follower_count"] , B["follower_count"] )

    if is_correct :
        score += 1
        print(f"You are right. Current score is {score}.")
    else:
        game_continue = False
        print(f"Sorry you are wrong. Final score is {score}.")





