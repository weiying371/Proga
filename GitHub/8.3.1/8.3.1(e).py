import math

x = float(input("Введіть x: "))
eps = float(input("Введіть eps: "))

term = x
s = term
n = 1

while abs(term) > eps:
    term *= -x * x / ((2 * n) * (2 * n + 1))
    s += term
    n += 1

print("sin(x) через ряд Тейлора =", s)
print("sin(x) з бібліотеки math =", math.sin(x))
print("Похибка =", abs(s - math.sin(x)))
