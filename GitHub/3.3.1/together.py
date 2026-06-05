from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Parallelogram import Parallelogram
from Circle import Circle
from Ball import Ball
from TriangularPyramid import TriangularPyramid
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from Cone import Cone
from TriangularPrism import TriangularPrism
import os

filenames = ["input01.txt", "input02.txt", "input03.txt"]
all_figures = []

current_dir = os.path.dirname(os.path.abspath(__file__))

for name in filenames:
    full_path = os.path.join(current_dir, name)

    if not os.path.exists(full_path):
        continue

    with open(full_path, "r", encoding="utf-8") as file:
        for line in file:
            p = line.split()
            if len(p) < 2:
                continue

            try:
                f_name = p[0]
                v = [float(x) for x in p[1:]]

                f = None
                if f_name == "Triangle":
                    f = Triangle(v[0], v[1], v[2])
                elif f_name == "Rectangle":
                    f = Rectangle(v[0], v[1])
                elif f_name == "Trapeze":
                    f = Trapeze(v[0], v[1], v[2], v[3])
                elif f_name == "Parallelogram":
                    f = Parallelogram(v[0], v[1], v[2])
                elif f_name == "Circle":
                    f = Circle(v[0])
                elif f_name == "Ball":
                    f = Ball(v[0])
                elif f_name == "TriangularPyramid":
                    f = TriangularPyramid(v[0], v[1])
                elif f_name == "QuadrangularPyramid":
                    f = QuadrangularPyramid(v[0], v[1], v[2])
                elif f_name == "RectangularParallelepiped":
                    f = RectangularParallelepiped(v[0], v[1], v[2])
                elif f_name == "Cone":
                    f = Cone(v[0], v[1])
                elif f_name == "TriangularPrism":
                    f = TriangularPrism(v[0], v[1], v[2], v[3])

                if f:
                    all_figures.append(f)
            except (IndexError, ValueError):
                continue


if all_figures:
    best = all_figures[0]
    for f in all_figures:
        if f.volume() > best.volume():
            best = f

    print(f"Фігура з найбільшою мірою: {type(best).__name__}")
    print(f"Міра (Площа/Об'єм) = {best.volume():.2f}")
