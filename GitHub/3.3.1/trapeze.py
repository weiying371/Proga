from Figure import Figure
import math

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimension(self): return 2

    def perimetr(self): return self.a + self.b + self.c + self.d

    def square(self):
        if self.a == self.b: return 0
        diff = self.a - self.b
        return ((self.a+self.b)/2) * math.sqrt(abs(self.c**2 - ((diff**2 + self.c**2 - self.d**2)/(2*diff))**2))

    def volume(self): return self.square()
