from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
    
    def write_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.l_score,align="center",font=("Fira code",30,"italic "))
        self.goto(100,250)
        self.write(self.r_score,align="center",font=("Fira code",30,"italic "))
