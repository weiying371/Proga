from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h_val = h

    def dimension(self): return 3

    def height(self): return self.h_val

    def squareBase(self): return super().square()

    def volume(self): return (1/3) * self.squareBase() * self.h_val
