from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()

    # (left point) score condition
    if ball.xcor() > 385:
        score.l_point()
        ball.reset()

    # (right point) score condition
    if ball.xcor() < -385:
        score.r_point()
        ball.reset()

    # bounce paddle condition
    if ball.distance(r_paddle) < 50 and ball.xcor() >= (r_paddle.xcor() - 15):
        ball.bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() <= (l_paddle.xcor() + 15):
        ball.bounce()

    # counce wall condition
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce()






screen.exitonclick()