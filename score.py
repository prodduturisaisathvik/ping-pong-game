from turtle import Turtle
from turtle import Screen
test=True


class Scoreboard_1(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-350, 300)
        self.write(f"SCORE OF A:{self.score}", align="center", font=("arial", 24, "normal"))
        self.screen.tracer(1)

    def increase_score(self):
        self.score += 1
        self.write(f"SCORE OF A:{self.score}", align="center", font=("arial", 24, "normal"))

    def clean(self):
        self.clear()


class Scoreboard_2(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(350, 300)
        self.write(f"SCORE OF B:{self.score}", align="center", font=("arial", 24, "normal"))
        self.screen.tracer(1)

    def increase_score(self):
        self.score += 1
        self.write(f"SCORE OF B:{self.score}", align="center", font=("arial", 24, "normal"))

    def clean(self):
        self.clear()


class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=("arial", 50, "normal"))



class A(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-600, 300)
        self.write("A", align="center", font=("arial", 24, "normal"))
        self.screen.tracer(1)


class B(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(600, 300)
        self.write("B", align="center", font=("arial", 24, "normal"))
        self.screen.tracer(1)








class Compare_score:

    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.color("white")

    def compare_score_1(self):
        self.tim.goto(0, -100)
        self.tim.write(
            "A WINS",
            align="center",
            font=("Arial", 50, "normal")
        )

    def compare_score_2(self):
        self.tim.goto(0, -100)
        self.tim.write(
            "B WINS",
            align="center",
            font=("Arial", 50, "normal")
        )

    def compare_score_3(self):
        self.tim.goto(0, -100)
        self.tim.write(
            "A TIE",
            align="center",
            font=("Arial", 50, "normal")
        )


