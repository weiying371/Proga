from turtle import mainloop, speed, setheading, pendown, penup, goto

from Leaves import Leaves
from Petals import Petals
from Stem import Stem

class Flowers:
    def __init__(self, color, angle):
        self._angle = angle
        self._color = color
        self._Stem = Stem()
        self._Leaves = Leaves()
        self._Petals = Petals(self._color)

    def draw(self, x, y):
        penup()
        goto(x, y)
        setheading(self._angle)
        pendown()
        self._Stem.draw(80)
        self._Leaves.draw("left")
        self._Stem.draw(80)
        self._Petals.draw()




if __name__ == '__main__':
    speed(0)

    flower_data = [("violet", 110), ("hot pink", 90), ("orange", 70)]

    for color, angle in flower_data:
        my_flower = Flowers(color, angle)
        my_flower.draw(0, -200)

mainloop()
