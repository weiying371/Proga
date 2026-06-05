from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h_val = h

    def dimension(self): return 3

    def height(self): return self.h_val

    def squareBase(self): return super().square()

    def volume(self): return self.squareBase() * self.h_val
