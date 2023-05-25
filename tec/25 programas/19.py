def f(x):
    return 1 / x

def area_bajo_curva(a, b, n):
    h = (b - a) / n  # Ancho de cada subintervalo
    suma = 0.5 * (f(a) + f(b))  # Suma de los valores en los extremos

    for i in range(1, n):
        x = a + i * h
        suma += f(x)

    area = h * suma
    return area

# Intervalo [1, 10] con 100 subintervalos
a = 1
b = 10
n = 100

area = area_bajo_curva(a, b, n)
print("El área bajo la curva es:", area)
