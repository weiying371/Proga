from Figure import Figure
from turtle import *

class Board(Figure):
    def draw(self, color):
        self.t.pencolor(color)
        self.t.pensize(2)

        for i in [-50, 50]:
            self.t.penup()
            self.t.goto(i, 150)
            self.t.pendown()
            self.t.goto(i, -150)

            self.t.penup()
            self.t.goto(-150, i)
            self.t.pendown()
            self.t.goto(150, i)
if __name__ == '__main__':
    b = Board("red")
    b.draw("red")

    mainloop()
