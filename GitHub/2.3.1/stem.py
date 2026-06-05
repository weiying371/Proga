import turtle
from turtle import penup, goto, setheading, pendown, pensize, color, forward


class Stem:
    def __init__(self, height=150, width=5, color="dark green"):
        self._color = color
        self._height = height
        self._width = width

    def draw(self, height):
        pensize(self._width)
        color(self._color)
        forward(height)

if __name__=='__main__':
    first_stem = Stem()
    print(first_stem.draw(30))

