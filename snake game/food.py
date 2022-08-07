from turtle import Turtle
from random import randint

class Food(Turtle):
    """Create the food in the Screen"""
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.new_location()

    def new_location(self):
        location=(randint(-280,280),randint(-280,280))
        self.goto(location)
