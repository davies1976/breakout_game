from turtle import Turtle


class Block(Turtle):
    def __init__(self, position_offset, row):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color("red")
        self.penup()
        self.goto((-350+(position_offset*75)), (250-(row*30)))
