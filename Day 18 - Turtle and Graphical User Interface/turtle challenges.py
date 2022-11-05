import random
import turtle
from turtle import Turtle , Screen
from random import Random
tim = Turtle()
# #challenge 1
# for _ in range(4):
#     tim.forward(150)
#     tim.left(90)

# #challenge 2
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#challenge 3
# color_list = ["red" , "green" , "blue" , "black" , "yellow" , "purple"]
# def drawshape(no_of_sides):
#     tim.color(random.choice(color_list))
#     angle = 360 / no_of_sides
#     for _ in range(no_of_sides):
#         tim.forward(100)
#         tim.left(angle)
# for i in range(3,11):
#     drawshape(i)

#challenge 4
directions = [0, 90 , 180 , 270]
tim.pensize(10)
tim.speed("fastest")
turtle.colormode(255)
def color_pic():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for _ in range(200):

    tim.color(color_pic())
    tim.forward(20)
    tim.setheading(random.choice(directions))

