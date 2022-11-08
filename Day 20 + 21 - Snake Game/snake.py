from turtle import Turtle , Screen
MOVE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        python = Turtle("triangle")
        python.penup()
        python.shapesize(stretch_len=1.2 , stretch_wid=1.2)
        python.color("white")
        self.snake_list.append(python)
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        python = Turtle("square")
        python.penup()
        python.color("white")
        python.speed("fastest")
        python.goto(position)
        self.snake_list.append(python)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

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

