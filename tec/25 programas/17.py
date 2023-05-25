import math

def f(x):
    return math.sin(x)

def encontrar_maximo(intervalo_a, intervalo_b, paso):
    maximo = float('-inf')
    x_maximo = None
    x = intervalo_a
    while x <= intervalo_b:
        y = f(x)
        if y > maximo:
            maximo = y
            x_maximo = x
        x += paso
    return x_maximo, maximo

# Parámetros de entrada
intervalo_a = 0
intervalo_b = 2
paso = 0.01

# Llamada a la función para encontrar el máximo
x_maximo, maximo = encontrar_maximo(intervalo_a, intervalo_b, paso)

# Imprimir el máximo relativo encontrado
print("El máximo relativo de la función en el intervalo [0, 2] es:", maximo)
print("Se alcanza en x =", x_maximo)
