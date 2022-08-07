from tkinter.tix import Tree
from turtle import Turtle
UP,DOWN,RIGHT,LEFT=90,270,0,180
BOUNDARY_X=400
BOUNDARY_Y=380
class Snake:
    def __init__(self) -> None:
        self.count=3
        self.position=0
        self.snake_list=[]
        self.create()
        self.head=self.snake_list[0]

    def create(self):
        for _ in range(3):
            val=Turtle("square")
            val.color("white")
            val.penup()
            val.setpos(self.position,0)
            self.position-=20
            self.snake_list.append(val)

    def move(self):
        for i in range(len(self.snake_list)-1,0,-1):
            self.snake_list[i].goto(*self.snake_list[i-1].pos())
        self.head.fd(20)

    def grow(self):
        val=Turtle("square")
        val.color("white")
        val.penup()

        val.goto(self.snake_list[-1].pos())
        self.snake_list.append(val)

    def up(self):
        if not self.head.heading()==DOWN:
            self.head.setheading(UP)


    def down(self):
        if not self.head.heading()==UP:
            self.head.setheading(DOWN)


    def right(self):
        if not self.head.heading()==LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if not self.head.heading()==RIGHT:
            self.head.setheading(LEFT)

    def check_wall_collision(self):
        position=self.head.pos()
        if position[0] > BOUNDARY_X or position[0] < -BOUNDARY_X or position[1] > BOUNDARY_Y or position[1] < -BOUNDARY_Y:
            return True
        return False

    def check_self_collision(self):
        for snake in self.snake_list[1:]:
            if self.head.distance(snake)<10:
                return True
        return False
    
    def reset_snake(self):
        for i in self.snake_list:
            i.goto(1000,1000)
        self.snake_list.clear()
        self.create()
        self.head=self.snake_list[0]
