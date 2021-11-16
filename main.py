from turtle import Screen
from paddle import Paddle
# from ball import Ball

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

# # create the ball and move it
# ball = Ball()

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

game_on = True

while game_on:
    screen.update()

# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score

screen.exitonclick()
