import random
import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()

    for seg in snake.snake_list:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()