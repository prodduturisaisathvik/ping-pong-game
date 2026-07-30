import time
from score import Scoreboard_2, Scoreboard_1,Game_over,A,B,Compare_score
from turtle import Screen
screen=Screen()
from paddle import Paddle_1
from ball import Ball
ball=Ball()
compare = Compare_score


screen.bgcolor("black")
screen.setup(1400,600)
screen.setup(width=1.0, height=1.0)
paddle=Paddle_1()
paddle.direction()
paddle.line()
paddle.boundary()
ball.ball()
score1=Scoreboard_1()
score2=Scoreboard_2()
a=A()
b=B()
ball.choice_1()





game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    if ball.player_name=="a":
        ball.move_a()
    elif ball.player_name=="b":
        ball.move_b()
    if ball.player_name=="":
        game_on = False
        game = Game_over()
        screen.tracer(0)
    if ball.tim.ycor()>280 or ball.tim.ycor()<-330:
        time.sleep(0.1)
        screen.update()
        ball.bounce()
    if ball.tim.distance(paddle.paddle1)<50 and ball.tim.xcor()<-630:
        ball.bounce_x()
        score1.clean()
        score1.increase_score()
    if ball.tim.distance(paddle.paddle2)<50 and ball.tim.xcor()>630:
        ball.bounce_x()
        score2.clean()
        score2.increase_score()
    if ball.tim.xcor()>650 or ball.tim.xcor()<-650:
        game_on=False
        game = Game_over()
        screen.tracer(0)




screen.exitonclick()
