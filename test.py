def leftside(self):
    new_x = -600
    new_y = random.randint(-300, 300)
    angle = radians(new_x + 50 / new_y + 50)
    self.tim.setheading(angle)
    dis = math, sqrt((new_x * new_x) + (new_y * new_y))
    self.tim.forward(dis)
    self.screen.listen()




def online(self):
    new_x1 = 0
    new_y1 = random.randint(-300, 300)
    angle_1 = radians(new_x1 + 50 / new_y1 - 50)
    self.tim.setheading(angle_1)
    dis = math.sqrt((new_x1 * new_x1) + (new_y1 * new_y1))
    self.tim.forward(dis)
    self.screen.listen()




def right(self):
    new_x2 = 600
    new_y2 = random.randint(-300, 300)
    angle_2 = radians(new_x2 + 50 / new_y2 + 50)
    self.tim.setheading(angle_2)
    dis = math, sqrt((new_x2 * new_x2) + (new_y2 * new_y2))
    self.tim.forward(dis)
    self.screen.listen()





def setangle(self):
    paddle = Paddle_1()
    if paddle.choice_1()=="a":
        self.ask=random.randint(135,225)
    else:
        self.ask=random.choice([random.randint(315,360),random.randint(0,45)])
def move(self):
    paddle = Paddle_1()
    self.tim.setheading(self.ask)
    while game_over:
        self.tim.forward(20)
        if self.tim.distance(paddle.paddle1) <10 or self.tim.distance(paddle.paddle2) <10:
            self.tim





    def game_on(self):
        tom=Turtle()
        tom.hideturtle()
        tom.color("white")
        tom.penup()
        tom.goto(0,300)
        tom.pendown()
        tom.write("game_on", align="center", font=("arial", 24, "normal"))



    def project_score(self):
        self.tom.score=0
        self.tom = Turtle()
        self.tom.hideturtle()
        self.tom.color("white")
        self.tom.penup()
        self.tom.goto(-350, 300)
        self.tom.pendown()
        self.tom.write(self.tom.score, align="center", font=("arial", 24, "normal"))

        self.tim.score = 0
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.penup()
        self.tim.goto(350, 300)
        self.tim.pendown()
        self.tim.write(self.tim.score, align="center", font=("arial", 24, "normal"))












class Ball:

    def __init__(self):
        self.screen=Screen()
        self.tim=Turtle()
        self.x_move=10
        self.y_move=10
        self.player_name=""
        pass

    def ball(self):
        self.tim.shape("circle")
        self.tim.color("white")
        self.tim.penup()
        self.tim.shapesize(math.radians(20))
        self.tim.goto(0, 0)
        self.screen.listen()

    def move(self):
        new_x = self.tim.xcor() + self.x_move
        new_y = self.tim.ycor() + self.y_move
        self.tim.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1





import time
from score import Scoreboard_2, Scoreboard_1, Game_over
from turtle import Screen

screen = Screen()
from paddle import Paddle_1
from ball import Ball

ball = Ball()

screen.bgcolor("black")
screen.setup(1400, 600)
paddle = Paddle_1()
paddle.direction()
paddle.line()
ball.ball()
score1 = Scoreboard_1()
score2 = Scoreboard_2()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.tim.ycor() > 350 or ball.tim.ycor() < -350:
        time.sleep(0.1)
        screen.update()
        ball.bounce()
    if ball.tim.distance(paddle.paddle1) < 50 and ball.tim.xcor() < -630:
        ball.bounce_x()
        score1.clean()
        score1.increase_score()
    if ball.tim.distance(paddle.paddle2) < 50 and ball.tim.xcor() > 630:
        ball.bounce_x()
        score2.clean()
        score2.increase_score()
    if ball.tim.xcor() > 650 or ball.tim.xcor() < -650:
        game_on = False
        game = Game_over()
        screen.tracer(0)

screen.exitonclick()

