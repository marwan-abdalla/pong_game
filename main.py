from turtle import Turtle, Screen
import time
from players import Players
from ball import Ball
from score import Score

screen = Screen()
turtle = Turtle()
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
screen.setup(height=800, width=1200)
score = Score()

paddle_1 = Players((-590, 0))
paddle_2 = Players((580, 0))

ball = Ball()

screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up_2, "Up")
screen.onkey(paddle_2.down_2, "Down")


game_running = True

while game_running:
    screen.update()
    ball.move()

    if ball.ycor() < -350 or ball.ycor() > 390:
        ball.bounce()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 500:
        ball.paddle_bounce()

    if ball.distance(paddle_1) < 50 and ball.xcor() < -500:
        ball.paddle_bounce()

    if ball.xcor() > 550:
        ball.resetting_position()
        score.update_scoreboard1()

    if ball.xcor() < -570:
        ball.resetting_position()
        score.update_scoreboard2()


screen.exitonclick()




