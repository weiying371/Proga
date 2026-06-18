n = int(input("Введіть n: "))

p = 1

for i in range(1, n + 1):
    p *= 1 / (i + 1)

print("Pn =", p)
