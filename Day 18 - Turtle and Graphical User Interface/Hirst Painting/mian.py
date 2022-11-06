import random
import turtle
from turtle import Turtle , Screen

tim = Turtle()
turtle.colormode(255)

color_list = [(202, 164, 110), (136, 239, 243), (149, 75, 50), (22, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (132, 76, 165)]

tim.penup()
tim.hideturtle()
tim.setheading(230)
tim.forward(330)
tim.setheading(0)
tim.speed("fastest")
def reset_position():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    reset_position()

screen = Screen()
screen.exitonclick()