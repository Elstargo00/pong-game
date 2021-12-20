from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.setheading(45)
        self.velocity = 10

    def move(self):
        self.forward(self.velocity)

    def bounce(self):
        self.setheading(self.heading() - 90)
        self.velocity += 1

    def reset(self):
        self.setheading(self.heading() - 180)
        self.velocity = 10
        self.goto(0, 0)


