import math

class Rational:
    def __init__(self, *args):
        if len(args) == 2:
            self._n = int(args[0])
            self._d = int(args[1])
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                if '/' in arg:
                    parts = arg.split('/')
                    self._n, self._d = int(parts[0]), int(parts[1])
                else:
                    self._n, self._d = int(arg), 1
            elif isinstance(arg, Rational):
                self._n, self._d = arg._n, arg._d
            else:
                self._n, self._d = int(arg), 1

        if self._d == 0:
            raise ValueError("Знаменник не може бути нулем!")
        self.simplify()

    def simplify(self):
        common = math.gcd(self._n, self._d)
        self._n //= common
        self._d //= common
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __add__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __getitem__(self, key):
        if key == "n": return self._n
        if key == "d": return self._d
        raise KeyError("Ключ має бути 'n' або 'd'")

    def __str__(self):
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f"Rational('{self._n}/{self._d}')"
