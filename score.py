from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 290)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 290)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def update_scoreboard1(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def update_scoreboard2(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()




