from Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimension(self): return 2

    def perimetr(self): return 2 * (self.a + self.b)

    def square(self): return self.a * self.b

    def volume(self): return self.square()
