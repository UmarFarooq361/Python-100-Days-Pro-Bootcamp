from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial" , 30 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        # self.goto(100 , 260)
        # self.write(self.r_score, align=ALIGNMENT, font= FONT)
        # self.goto(-100, 260)
        # self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(100 , 260)
        self.write(self.r_score, align=ALIGNMENT, font= FONT)
        self.goto(-100, 260)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()


