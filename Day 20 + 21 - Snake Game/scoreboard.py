from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial" , 20 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.SCORE = 0
        self.color("white")
        self.penup()
        self.goto(0 , 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.SCORE}", align=ALIGNMENT, font= FONT)
    def increase_score(self):
        self.SCORE +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font= FONT)

