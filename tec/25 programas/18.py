def f(x):
    return x ** 2

n = 1000
dx = 1.0 / n

area_total = 0.0

for i in range(n):
    x = (i + 0.5) * dx
    area_total += f(x) * dx

print("El área debajo de la curva es:", area_total)
