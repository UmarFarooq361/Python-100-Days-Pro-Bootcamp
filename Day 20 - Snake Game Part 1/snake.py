from turtle import Turtle , Screen
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for _ in range(0, 3):
            python = Turtle("square")
            python.penup()
            python.color("white")
            python.goto(self.x, self.y)
            self.snake_list.append(python)
            self.x -= 20
    def move(self):
        for py in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[py - 1].xcor()
            new_y = self.snake_list[py - 1].ycor()
            self.snake_list[py].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

