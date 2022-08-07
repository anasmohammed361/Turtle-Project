from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen=Screen()
screen.screensize(600,600)
screen.title("Snakeeee")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
score=ScoreBoard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_status=True
while game_status:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        food.new_location()
        snake.grow()
        score.update_score()
    
    if snake.check_wall_collision():
        snake.reset_snake()
        score.upadate_highscore()
        # game_status=False
        # score.game_over()
    
    if snake.check_self_collision():
        snake.reset_snake()
        score.upadate_highscore()
        # game_status=False
        # score.game_over()        



screen.exitonclick()