from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        with open("highscore.txt","r") as f:
           self.highscore=int(f.read())
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score+=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}",move=False,align="center",font=("Arial",20,"bold italic"))

    def reset_score(self):
        self.upadate_highscore()
        self.write_score()
        
    def upadate_highscore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore.txt","w") as f:
                f.write(f"{self.highscore}")
        self.score=0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",move=False,align="center",font=("Arial",20,"bold italic"))