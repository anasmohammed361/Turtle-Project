from turtle import Screen
from bar import Bar
from ball import Ball
from time import sleep
from score_board import ScoreBoard

ball_speed=20
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

left_bar=Bar(-390,0)
right_bar=Bar(390,0)
ball=Ball()
score_board=ScoreBoard()

screen.update()
screen.listen()

screen.onkey(left_bar.move_up,"w")
screen.onkey(left_bar.move_down,"s")

screen.onkey(right_bar.move_up,"Up")
screen.onkey(right_bar.move_down,"Down")


ball.move()
game_status=True

score_board.write_score()
# screen.tracer(1)

while game_status:
    sleep(0.05)
    ball.forward(ball_speed)
    if ball.check_collision_with_wall():
        ball.change_direction_wall()


    if ball.distance(right_bar) <50 and ball.xcor()>370:
        ball_speed= ball_speed+1 if ball_speed<35 else ball_speed
        ball.change_direction_bar()

    if ball.distance(left_bar) <50 and ball.xcor() < -370:
        ball_speed= ball_speed+1 if ball_speed<35 else ball_speed
        ball.change_direction_bar()

    res_tup=ball.check_if_ball_is_in_board()

    if res_tup:
        ball.reset_ball()
        if (res_tup[1]==1):
            score_board.l_score+=1  
        else:
            score_board.r_score+=1
        score_board.write_score()
    screen.update()


screen.exitonclick()