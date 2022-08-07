import time
from turtle import Screen
from player import Player
from car_manager import CarManager,Car
from scoreboard import Scoreboard

car=CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
score_board=Scoreboard()
screen.listen()
screen.onkey(player.move_up,"Up")

score_board.write_level()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move_cars()

    if player.check_finish():
        player.level_up()
        car.speed_cars()
        score_board.level_up()
    car.create_car()
    
    for i in car.all_cars:
        if player.distance(i) < 30:
            game_is_on=False
            score_board.game_over()

    screen.update()

screen.exitonclick()