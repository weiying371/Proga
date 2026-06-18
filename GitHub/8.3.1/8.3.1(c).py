def determinant(n):
    if n == 1:
        return 2

    if n == 2:
        return 1

    d1 = 2
    d2 = 1

    for _ in range(3, n + 1):
        d = 2 * d2 - 3 * d1
        d1 = d2
        d2 = d

    return d2


n = int(input("Введіть n: "))
print("Визначник =", determinant(n))
