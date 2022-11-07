import random
import turtle
import time
from turtle import Turtle , Screen
from snake import Snake


screen = Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)
is_game_on = True

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()




screen.exitonclick()