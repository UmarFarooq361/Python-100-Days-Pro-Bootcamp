import random
import turtle
from turtle import Screen , Turtle
from paddles import Paddles
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800 , height= 600)
screen.bgcolor("black")
screen.title("Pong ")
screen.listen()
r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350 , 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()
screen.onkeypress(r_paddle.move_up , "Up")
screen.onkeypress(r_paddle.move_down , "Down")
screen.onkeypress(l_paddle.move_up , "w")
screen.onkeypress(l_paddle.move_down , "s")

game_is_on =True
while game_is_on:
    time.sleep(ball.speed_move)
    ball.move()
    screen.update()
    scoreboard.r_score
    scoreboard.l_score
    if  ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce()
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 310 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.paddle_bounce()

    #left paddle miss
    if  ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    # right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()