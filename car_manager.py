import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars=[]
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance==1:
            new_car=Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(0.5, 1.0)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)
    def move_car(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance+=MOVE_INCREMENT