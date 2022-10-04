from turtle import Turtle
from json import load
import time
FONT=("Fira code",7,"normal")

class State(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.found=0
        self.locations=load(open("/home/anasmohammed361/vs/Python Course/Turtle/india_map_game/json/states_with_coords.json"))
        state=load(open("/home/anasmohammed361/vs/Python Course/Turtle/india_map_game/json/states.json"))
        self.states=list(state.values())
        self.penup()
        self.hideturtle()

    def check_state(self,entered_state:str):
        if entered_state in self.states:
            self.showturtle()
            self.found+=1
            self.goto(*self.locations.get(entered_state))
            self.hideturtle()
            self.write(f"{entered_state}",align="center",font=FONT)
            self.goto(0,0)
            time.sleep(0.5)

    def complete(self):
        self.goto(0,0)
        self.write("Hurray you Found all the States!!!",align="Center",font=("Fira code",17,"italic"))

