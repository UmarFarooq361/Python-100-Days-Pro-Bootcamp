import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down,"Down")
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()

    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_score()