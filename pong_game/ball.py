from turtle import Turtle
from random import choice

DEGREES=[45,45+90,45+180,45+270]
TOP,BOTTOM=270,-270
LEFT,RIGHT=-390,390

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        

    def move(self,):
        self.degree=choice(DEGREES)
        self.setheading(self.degree)

    def check_collision_with_wall(self):
        if self.ycor()>=TOP or self.ycor() <= BOTTOM:
            return True
        return False

    def change_direction_wall(self):
        if self.heading() in [45,45+180]:
            new_head=self.heading()-90
            self.setheading(new_head)
        else:
            new_head=self.heading()+90
            self.setheading(new_head)

    def change_direction_bar(self):
        if self.heading() in [45,45+180]:
            new_head=self.heading()+90
            self.setheading(new_head)
        else:
            new_head=self.heading()-90
            self.setheading(new_head)

# 1-> Right 2-> Left

    def check_if_ball_is_in_board(self):
        if self.xcor() > RIGHT  :
            return (True,1)
        elif self.xcor() < LEFT:
            return (True,2)
        return False

    def reset_ball(self):
        self.goto(0,0)
        self.change_direction_bar()
