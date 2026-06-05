from Figure import Figure

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self): return 3

    def squareSurface(self): return 4 * 3.1415 * (self.r ** 2)

    def volume(self): return (4/3) * 3.1415 * (self.r ** 3)
