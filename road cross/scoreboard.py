FONT = ("Courier", 20, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270,250)
        self.level=1
        self.color("black")
    
    def write_level(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)
    
    def level_up(self):
        self.level+=1
        self.write_level()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)