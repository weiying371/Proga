import math

class Triangles:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimetr(self):
        return self._a + self._b + self._c

    def square(self):
        p = self.perimetr() / 2
        sq = p * (p - self._a) * (p - self._b) * (p - self._c)
        return math.sqrt(max(0, sq))

class Rectangles:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def perimetr(self):
        return 2*(self._a + self._b)

    def square(self):
        return self._a * self._b

class Trapeze:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def perimetr(self):
        return self._a + self._b + self._c + self._d

    def square(self):
        a, b, c, d = self._a, self._b, self._c, self._d
        if a == b:
            return 0
        h_sq = c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))) ** 2
        return ((a + b) / 2) * math.sqrt(max(0, h_sq))

class Parallelogram:
    def __init__(self, a, b, h):
        self._a = a
        self._b = b
        self._h = h

    def perimetr(self):
        return 2 * (self._a + self._b)

    def square(self):
        return self._a * self._h

class Circles:
    def __init__(self, r):
        self._r = r

    def perimetr(self):
        return 2 * math.pi * self._r

    def square(self):
        return math.pi * (self._r ** 2)




if __name__ == '__main__':
    for i in range(1, 4):
        try:
            f = open(f"input0{i}.txt", "r")
        except FileNotFoundError:
            continue

        max_square = -float('inf')
        max_square_shape = None

        max_perimetr = -float('inf')
        max_perimetr_shape = None

        print(f"Обробка файлу input0{i}.txt")

        for line in f:
            try:
                parts = line.split()
                if not parts: continue

                name = parts[0]
                params = [float(x) for x in parts[1:]]

                if name == "Triangle":
                    q = Triangles(params[0], params[1], params[2])
                elif name == "Rectangle":
                    q = Rectangles(params[0], params[1])
                elif name == "Trapeze":
                    q = Trapeze(params[0], params[1], params[2], params[3])
                elif name == "Parallelogram":
                    q = Parallelogram(params[0], params[1], params[2])
                elif name == "Circle":
                    q = Circles(params[0])
                else:
                    continue

                square = q.square()
                perimetr = q.perimetr()
                print(f"{name}: S={square:.2f}, P={perimetr:.2f}")

                if square > max_square:
                    max_square = square
                    max_square_shape = q

                if perimetr > max_perimetr:
                    max_peri_val = perimetr
                    max_perimetr_shape = q

            except (ValueError, IndexError):
                continue

        f.close()

        print("\nResults of the file:")
        if max_square_shape:
            print(f"Max square: {type(max_square_shape).__name__} ({max_square:.2f})")
        if max_perimetr_shape:
            print(f"Max perimetr: {type(max_perimetr_shape).__name__} ({max_perimetr:.2f})")


        with open("result_1.3.1.txt", "a", encoding="utf-8") as out_file:
            out_file.write(f"Результати для файлу input0{i}.txt\n")
            if max_square_shape:
                out_file.write(f"Максимальна площа: {type(max_square_shape).__name__} ({max_square:.2f})\n")
            if max_perimetr_shape:
                out_file.write(f"Максимальний периметр: {type(max_perimetr_shape).__name__} ({max_perimetr:.2f})\n")
            out_file.write("-" * 30 + "\n")


