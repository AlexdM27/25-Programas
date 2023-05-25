import random

# Función para generar enteros aleatorios entre 0 y 100
def generar_entero_aleatorio():
    return random.randint(0, 100)

# Contadores para pares e impares
contador_pares = 0
contador_impares = 0

# Generar 1000 enteros aleatorios y contar pares e impares
for _ in range(1000):
    numero = generar_entero_aleatorio()
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

# Imprimir resultados
print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)
