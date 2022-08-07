from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self) -> None:
        self.all_cars=[]
        self.STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE
        self.MOVE_INCREMENT = MOVE_INCREMENT
    
    def create_car(self):
        if randint(1,6)==1:
            car=Car()
            self.all_cars.append(car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def speed_cars(self):
        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.goto((280,randint(-250,250)))
