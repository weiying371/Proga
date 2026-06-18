n = int(input("Введіть n: "))

a = [0] * (n + 1)

if n >= 1:
    a[1] = 0

if n >= 2:
    a[2] = 1

for k in range(3, n + 1):
    a[k] = a[k - 1] + k * a[k - 2]

s = 0

for k in range(1, n + 1):
    s += (2 ** k) * a[k]

print("Sn =", s)
