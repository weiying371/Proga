from turtle import begin_fill, color, setheading, end_fill, circle, left, right, exitonclick, heading


class Leaves:
    def __init__(self, color = "dark green"):
        self._color = color

    def draw(self, side):
        color(self._color)
        current_h = heading()

        if side == "left":
            setheading(current_h + 45)
        else:
            setheading(current_h - 45)

        begin_fill()

        for j in range(2):
            circle(60, 90)  # Радіус 60, кут 90 для плавнішої форми
            left(90)

        end_fill()

        setheading(current_h)

if __name__=='__main__':
    first_leaf = Leaves()
    print(first_leaf.draw(left))


