from turtle import Turtle,Screen
t=Turtle()
screen=Screen()

def move_forward():
    t.fd(10);
def move_backward():
    t.back(10)
def right_rotate():
    t.right(10)
def left_rotate():
    t.left(10)
def clear_screen():
    t.setpos(0,0)
    t.clear()
    t.setheading(0)
screen.listen()
screen.onkeypress(move_forward,"Up")
screen.onkeypress(move_backward,"Down")
screen.onkeypress(right_rotate,"Right")
screen.onkeypress(left_rotate,"Left")
screen.onkeypress(clear_screen,"space")
screen.exitonclick()