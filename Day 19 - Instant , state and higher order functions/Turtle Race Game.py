import random
import turtle
from turtle import Turtle , Screen

screen = Screen()
screen.setup(width=500 , height= 400)
screen.listen()
user_bet = screen.textinput(title="Race a bet" , prompt="Which turtle will win the race ? choose your color")
colors = ["blue" , "green", "red" , "purple" , "yellow" , "black" , "orange"]

x = -240
y = -100
is_race_on =   False
all_racers = []
for i in range(0,7):

    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_racers.append(new_turtle)
    y += 30

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_racers:
        if turtle.xcor()>220:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You won. The {winner} is the winner.")
            else:
                print(f"You loss. The {winner} is the winner.")

        rand_distance = random.randint(0 ,10)
        turtle.forward(rand_distance)



screen.exitonclick()