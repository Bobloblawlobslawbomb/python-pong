from turtle import Turtle

MOVE_DISTANCE = 20
MAX_Y = 260
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y == MAX_Y:
            pass
        else:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y == -MAX_Y:
            pass
        else:
            self.goto(self.xcor(), new_y)
