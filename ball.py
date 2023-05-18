from turtle import Turtle

move_dist = 10

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_dist = move_dist
        self.y_move_dist = move_dist
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1

    def reset_position(self):
        self.goto(0, -240)
        self.y_move_dist = 10
