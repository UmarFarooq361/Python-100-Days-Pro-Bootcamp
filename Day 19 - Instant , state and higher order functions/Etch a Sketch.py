import random
import turtle
from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()
screen.listen()

def forwards():
    tim.forward(10)
def backwards():
    tim.backward(10)
def count_clock():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

turtle.onkeypress(forwards, "w")
turtle.onkeypress(backwards, "s")
turtle.onkeypress(count_clock, "a")
turtle.onkeypress(clockwise, "d")
turtle.onkey(clear_screen, "c")


screen.exitonclick()