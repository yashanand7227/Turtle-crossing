import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
user = Player()
car_manager = CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(user.move_turtle, 'Up')
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if user.distance(car) < 20:
            scoreboard.game_over()
            game_is_on=False

    if user.ycor() > 280:
        user.reset_turtle()
        car_manager.increase_speed()
        scoreboard.update_level()



screen.exitonclick()