N = int(input("Ingrese el valor de N: "))

numeros = []
for i in range(N):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numeros.sort()

print("Números en orden de magnitud creciente:")
for numero in numeros:
    print(numero)
