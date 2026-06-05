from Figure import Figure
from turtle import *
class Cross(Figure):
    def draw(self, color):
        self.t.pencolor(color)
        self.t.pensize(4)
        size = 30

        for angle in [45, 135, 225, 315]:
            self.t.penup()
            self.t.goto(self.x, self.y)
            self.t.setheading(angle)
            self.t.pendown()
            self.t.forward(size)

class Zero(Figure):
    def draw(self, color):
        self.t.pencolor(color)
        self.t.pensize(4)
        self.t.penup()

        self.t.goto(self.x, self.y - 30)
        self.t.setheading(0)
        self.t.pendown()
        self.t.circle(30)

if __name__ == '__main__':
    c = Cross("blue",)
    c.draw("blue")


    mainloop()
