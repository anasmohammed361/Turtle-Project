from turtle import Screen
import time
from states import State
screen=Screen()
state=State()
screen.title("Inida Map Game")
screen.bgpic("india.gif")
screen.setup(width=600,height=800)
while state.found<=28:
    value=screen.textinput(f"{self.found}/29 States found","Enter a state :").title()
    print(value)
    state.check_state(value)
state.complete()
screen.exitonclick()
