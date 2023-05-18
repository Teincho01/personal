import turtle as tr
from turtle import Turtle

move_distance = 70

class Paddle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("steel blue")
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 10)
        self.goto(0, -280)

    def move_left(self):
        self.backward(move_distance)

    def move_right(self):
        self.forward(move_distance)


