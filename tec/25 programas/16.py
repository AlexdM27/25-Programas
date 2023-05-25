import math

def f(x):
    return math.sin(x) - math.cos(x)

def encontrar_raiz(intervalo_a, intervalo_b, tolerancia):
    a = intervalo_a
    b = intervalo_b
    while (b - a) > tolerancia:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Parámetros de entrada
intervalo_a = 0
intervalo_b = 1
tolerancia = 0.0001

# Llamada a la función para encontrar la raíz
raiz = encontrar_raiz(intervalo_a, intervalo_b, tolerancia)

# Imprimir la raíz encontrada
print("La raíz de la función en el intervalo [0, 1] es:", raiz)
