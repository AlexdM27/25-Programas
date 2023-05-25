libras = float(input("Ingresa el número de libras: "))
onzas = float(input("Ingresa el número de onzas: "))

total_onzas = libras * 16 + onzas
kilogramos = total_onzas * 0.0283495

print(f"{libras} libras y {onzas} onzas equivalen a {kilogramos} kilogramos")
