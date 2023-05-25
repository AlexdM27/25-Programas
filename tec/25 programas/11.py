def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

contador_primos = 0
rango = range(2, 101)

for numero in rango:
    if es_primo(numero):
        contador_primos += 1

probabilidad = contador_primos / len(rango)
print("La probabilidad de que un número entre 2 y 100 sea primo es:", probabilidad)
