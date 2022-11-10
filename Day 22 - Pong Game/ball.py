from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("blue")
        # self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
         self.y_move *= -1
    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.speed_move = 0.1

    def paddle_bounce(self):
        self.x_move *= -1
        self.speed_move *= 0.9




