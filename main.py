from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Python Pong"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

left_score = 0
right_score = 0

game_on = True


while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        left_score += 1
        ball.home()
        ball.bounce_paddle()
        ball.bounce_wall()
        print(f"left point total: {left_score}")

    if ball.xcor() < -380:
        right_score += 1
        ball.home()
        ball.bounce_paddle()
        ball.bounce_wall()
        print(f"right point total: {right_score}")


# detect when paddle misses
# keep score

screen.exitonclick()
