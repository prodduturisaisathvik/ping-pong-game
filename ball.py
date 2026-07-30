from turtle import Turtle,Screen
import math,random

import paddle
from paddle import game_over
from paddle import Paddle_1
class Ball:

    def __init__(self):
        self.screen=Screen()
        self.tim=Turtle()
        self.x_move=10
        self.y_move=10
        self.player_name=""
        pass

    def ball(self):
        self.screen.tracer(0)
        self.tim.shape("circle")
        self.tim.color("white")
        self.tim.penup()
        self.tim.shapesize(math.radians(40))
        self.tim.goto(0, 0)
        self.screen.listen()
        self.screen.tracer(1)

    def move_a(self):
        new_x = self.tim.xcor() - self.x_move
        new_y = self.tim.ycor() + self.y_move
        self.tim.goto(new_x, new_y)




    def move_b(self):
        new_x = self.tim.xcor() + self.x_move
        new_y = self.tim.ycor() + self.y_move
        self.tim.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def choice_1(self):
        self.player_name = self.screen.textinput(
            title="who is going to start first",
            prompt="Enter A or B"
        )
        self.screen.listen()
