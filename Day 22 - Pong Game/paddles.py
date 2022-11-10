from turtle import Turtle

class Paddles(Turtle):
    def __init__(self, position):
        super(Paddles, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # self.x_pos = position[0]
        # self.y_pos = position[1]
        self.goto(position)

    def move_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)
        # self.screen.update()

    def move_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
        # self.screen.update()



