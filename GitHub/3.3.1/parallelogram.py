from Figure import Figure

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, h_val = a, b, h
        self.h_val = h_val

    def dimension(self): return 2

    def perimetr(self): return 2 * (self.a + self.b)

    def square(self): return self.a * self.h_val

    def volume(self): return self.square()
