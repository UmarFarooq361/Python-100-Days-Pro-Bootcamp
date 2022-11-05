import random
import turtle
from turtle import Turtle , Screen
from random import Random
#challenge 5

tim = Turtle()
directions = [0, 90 , 180 , 270]
tim.pensize(1)
tim.speed("fastest")
turtle.colormode(255)
def color_pic():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb
def draw_spiroghraph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(color_pic())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spiroghraph(5)

tim.hideturtle()

screen = Screen()
screen.exitonclick()