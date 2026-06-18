import math
import os


# 7.3.1. Клас для помилок ділення на нуль
class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може бути нулем!"):
        self.message = message
        super().__init__(self.message)


# 7.3.2. Клас для некоректних даних в арифметичних операціях
class RationalValueError(ValueError):
    def __init__(self, message="Некоректні дані для арифметичної операції"):
        self.message = message
        super().__init__(self.message)


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
                    self._n = int(parts[0])
                    self._d = int(parts[1])
                else:
                    self._n = int(arg)
                    self._d = 1
            elif isinstance(arg, Rational):
                self._n = arg._n
                self._d = arg._d
            elif isinstance(arg, int):
                self._n = arg
                self._d = 1

        if self._d == 0:
            raise RationalError()
        self.simplify()

    def simplify(self):
        common = math.gcd(self._n, self._d)
        self._n //= common
        self._d //= common
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    # Оновлений метод для виконання завдання 7.3.2
    def to_rational(self, other):
        if isinstance(other, (int, Rational)):
            return Rational(other)
        if isinstance(other, str):
            try:
                return Rational(other)
            except (ValueError, RationalError):
                raise RationalValueError(f"Неможливо перетворити рядок '{other}' на Rational")

        # Використовуємо RationalValueError замість TypeError
        raise RationalValueError(f"Тип {type(other)} не підтримується для операцій")

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
        if other._n == 0:
            raise RationalError("Ділення на нуль")
        return Rational(self._n * other._d, self._d * other._n)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n": return self._n
        if key == "d": return self._d
        raise KeyError("Ключ має бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            if value == 0:
                raise RationalError()
            self._d = value
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")
        self.simplify()

    def __str__(self):
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f"Rational('{self._n}/{self._d}')"


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

    final_expr = " ".join(processed_parts)
    return eval(final_expr, {"Rational": Rational})


def main():
    input_file = 'input'  # Переконайтеся, що файл називається саме так (без .txt), як у вашому коді

    if not os.path.exists(input_file):
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            try:
                result = evaluate_rational_expression(line)
                print(f"Рядок {line_num}: {line} = {result} (десятковий: {result():.4f})")
            except RationalError as e:
                print(f"Помилка знаменника (7.3.1) у рядку {line_num}: {e}")
            except RationalValueError as e:
                print(f"Помилка значення (7.3.2) у рядку {line_num}: {e}")
            except Exception as e:
                print(f"Інша помилка у рядку {line_num}: {e}")


if __name__ == "__main__":
    main()
