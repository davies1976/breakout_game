from turtle import Turtle

START_PLAYER_POSITION = (0, -250)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4.5, stretch_wid=0.75)
        self.color("blue")
        self.penup()
        self.goto(START_PLAYER_POSITION)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
