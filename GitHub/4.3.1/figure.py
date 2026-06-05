import turtle

class Figure:
    def __init__(self, color="black"):
        self.x = 0
        self.y = 0
        self.color = color

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color):
        pass

    def show(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.draw(self.color)

    def hide(self):
        self.draw("white")
