import math

n = 52  # Número total de cartas en la baraja
r = 5   # Número de cartas en cada mano

# Calcula las combinaciones utilizando la fórmula
combinaciones = math.comb(n, r)

print("El número de manos posibles es:", combinaciones)
