from Figure import Figure

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self): return 2

    def perimetr(self): return 2 * 3.1415 * self.r

    def square(self): return 3.1415 * (self.r ** 2)

    def volume(self): return self.square()
