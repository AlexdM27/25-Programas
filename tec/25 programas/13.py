def calcular_permutaciones(n, r):
    if n < r:
        return "Error: n debe ser mayor o igual que r"
    
    resultado = 1
    for i in range(n, n - r, -1):
        resultado *= i
    
    return resultado

# Ejemplo de uso
n = int(input("Ingrese el número total de elementos (N): "))
r = int(input("Ingrese el número de elementos tomados a la vez (R): "))

permutaciones = calcular_permutaciones(n, r)
print("El número de permutaciones de", n, "cosas tomadas", r, "a la vez es:", permutaciones)
