from turtle import Turtle


class Players(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(position)
        self.line()

    def up(self):
        self.forward(50)

    def down(self):
        self.backward(50)

    def up_2(self):
        self.forward(50)

    def down_2(self):
        self.backward(50)

    def line(self):
        line = Turtle("square")
        line.color("white")
        line.hideturtle()
        line.pensize(7)

        def dotted_line():
            for i in range(10):
                line.forward(20)
                line.penup()
                line.forward(20)
                line.pendown()

        line.setheading(270)
        dotted_line()
        line.setheading(90)
        line.penup()
        line.goto(0, 0)
        dotted_line()



