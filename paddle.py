from turtle import Screen, Turtle
game_over=False
class Paddle_1:

    def __init__(self):
        self.screen = Screen()
        pass



    def createpaddle_1(self):
        self.screen.tracer(0)
        tim=Turtle()
        tim.penup()
        tim.setheading(0)
        tim.color("white")
        tim.shape("square")
        tim.shapesize(stretch_wid=1, stretch_len=5)
        tim.goto(-650,0)
        tim.left(90)
        self.screen.tracer(1)
        return tim






    def createpaddle_2(self):
        self.screen.tracer(0)
        tim=Turtle()
        tim.penup()
        tim.setheading(0)
        tim.color("white")
        tim.shape("square")
        tim.shapesize(stretch_wid=1, stretch_len=5)
        tim.goto(650,0)
        tim.left(90)
        self.screen.tracer(1)
        return tim




    def direction(self):
        self.paddle1 = self.createpaddle_1()
        self.paddle2 = self.createpaddle_2()
        def up1():
            if self.paddle1.ycor()> 239:
                self.paddle1.forward(0)
            else:
                self.paddle1.forward(20)


        def down1():
            if self.paddle1.ycor()<-280:
                self.paddle1.backward(0)
            else:
                self.paddle1.backward(20)

        def up2():
            if self.paddle2.ycor()>239:
                self.paddle2.forward(0)
            else:
                self.paddle2.forward(20)

        def down2():
            if self.paddle2.ycor()<-280:
                self.paddle2.backward(0)
            else:
                self.paddle2.backward(20)


        self.screen.listen()
        self.screen.onkeypress(up1, "q")
        self.screen.onkeyrelease(up1, "q")
        self.screen.onkeypress(up2, "p")
        self.screen.onkeyrelease(up2, "p")
        self.screen.onkeypress(down1, "a")
        self.screen.onkeyrelease(down1, "a")
        self.screen.onkeypress(down2, "l")
        self.screen.onkeyrelease(down2, "l")

    def line(self):
        game=False
        self.screen.tracer(0)
        tim=Turtle()
        tim.hideturtle()
        tim.penup()
        tim.color("white")
        tim.goto(0,-350)
        tim.left(90)
        while game==False:
            if tim.ycor() > 350:
                tim.forward(0)
                game=True
            else:
                tim.pendown()
                tim.forward(20)
                tim.penup()
                tim.forward(20)
        self.screen.tracer(1)




    def boundary(self):
        self.screen.tracer(0)
        tak=Turtle()
        tak.hideturtle()
        tak.penup()
        tak.color("white")
        tak.goto(660,300)
        tak.pendown()
        tak.goto(-660,300)
        tak.goto(-660,-350)
        tak.goto(660,-350)
        tak.goto(660, 300)
        self.screen.tracer(1)







