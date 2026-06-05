import turtle
import random

class Petals:
    def __init__(self, color):
        self.color = color


    def draw(self):
        turtle.color(self.color)
        turtle.begin_fill()
        for i in range(6):
            for j in range (2):
                turtle.circle(50, 60)
                turtle.left(120)
            turtle.left(60)
        turtle.end_fill()


if __name__=='__main__':
    first_flower = Petals("violet")
    print(first_flower.draw())
