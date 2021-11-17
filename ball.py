from turtle import Turtle

MOVE_DISTANCE = 10
BALL_SHAPE = "square"
BALL_COLOR = "white"
MOVE_SPEED = 0.1
MOVE_SPEED_MULTIPLER = 0.9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= MOVE_SPEED_MULTIPLER

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.bounce_paddle()
        self.bounce_wall()
