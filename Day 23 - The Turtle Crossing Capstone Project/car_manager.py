from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.all_cars = []
        self.speed_up = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        generate_car = random.randint(1,6)
        if generate_car == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid= 1 , stretch_len=2)
            car.penup()
            car.goto(300 , random.randint(-250 , 250))
            self.all_cars.append(car)



    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_up)

    def level_up(self):
        self.speed_up += MOVE_INCREMENT