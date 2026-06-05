from Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimension(self): return 2

    def perimetr(self): return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        rez = p * (p - self.a) * (p - self.b) * (p - self.c)
        return (abs(rez)) ** 0.5

    def volume(self): return self.square()
