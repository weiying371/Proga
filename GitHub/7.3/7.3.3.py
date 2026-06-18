import math
import os

class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може бути нулем!"):
        self.message = message
        super().__init__(self.message)

class RationalValueError(ValueError):
    def __init__(self, message="Некоректні дані для раціональних чисел"):
        self.message = message
        super().__init__(self.message)

class Rational:
    def __init__(self, *args):
        try:
            if len(args) == 2:
                self._n, self._d = int(args[0]), int(args[1])
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
                elif isinstance(arg, int):
                    self._n, self._d = arg, 1
                else:
                    raise RationalValueError(f"Тип {type(arg)} не підтримується")

            if self._d == 0:
                raise RationalError()
            self.simplify()
        except (ValueError, IndexError):
            raise RationalValueError("Некоректний формат рядка або числа для Rational")

    def simplify(self):
        common = math.gcd(self._n, self._d)
        self._n //= common
        self._d //= common
        if self._d < 0:
            self._n, self._d = -self._n, -self._d

    def to_rational(self, other):
        if isinstance(other, (int, Rational)): return Rational(other)
        if isinstance(other, str): return Rational(other)
        raise RationalValueError(f"Тип {type(other)} не підтримується")

    def __add__(self, other):
        other = self.to_rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)
    def __sub__(self, other):
        other = self.to_rational(other)
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)
    def __mul__(self, other):
        other = self.to_rational(other)
        return Rational(self._n * other._n, self._d * other._d)
    def __truediv__(self, other):
        other = self.to_rational(other)
        if other._n == 0: raise RationalError("Ділення на нуль")
        return Rational(self._n * other._d, self._d * other._n)

    def __str__(self): return f"{self._n}/{self._d}"
    def __repr__(self): return f"Rational('{self._n}/{self._d}')"

def evaluate_rational_expression(expression):
    for op in ['+', '-', '*', '/']:
        expression = expression.replace(op, f' {op} ')
    parts = expression.split()
    processed_parts = []
    for part in parts:
        if part in ['+', '-', '*', '/']:
            processed_parts.append(part)
        else:
            processed_parts.append(f'Rational("{part}")')
    return eval(" ".join(processed_parts), {"Rational": Rational})

class RationalList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable: self.append(item)

    def append(self, value):
        if not isinstance(value, (Rational, int, str)):
            raise RationalValueError(f"Непідтримуваний тип: {type(value).__name__}")
        try:
            new_rational = Rational(value)
            self._data.append(new_rational)
        except (RationalError, RationalValueError) as e:
            raise RationalValueError(f"Помилка 7.3.3: {e}")

    def __repr__(self): return f"RationalList({self._data})"

def main():
    input_file = 'input'
    r_list = RationalList()

    if not os.path.exists(input_file):
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line: continue
            try:
                result = evaluate_rational_expression(line)
                r_list.append(result)
                print(f"Рядок {line_num}: Результат {result} додано в список.")
            except (RationalError, RationalValueError) as e:
                print(f"Рядок {line_num}: Помилка: {e}")

    print("\nПідсумковий список RationalList:")
    print(r_list)

if __name__ == "__main__":
    main()
