from turtle import Turtle

class Bar(Turtle):
    def __init__(self,x_pos:float,y_pos:float) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.x_pos= x_pos
        self.y_pos=y_pos
        self.goto(self.x_pos,self.y_pos)
        self.shapesize(stretch_len=5)

    def move_up(self):
        if self.ycor()<240:
            self.forward(35)

    def move_down(self):
        if self.ycor()> -240:
            self.back(35)