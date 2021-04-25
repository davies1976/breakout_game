from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.move_speed = 2
        self.move_x = 0
        self.move_y = -3
        
    def move_ball(self):
        new_x = self.xcor() + self.move_x * self.move_speed
        new_y = self.ycor() + self.move_y * self.move_speed
        self.goto(new_x, new_y)

    def bounce_ball(self):
        self.move_y *= -1
