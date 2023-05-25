def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

# Lectura de temperatura en Kelvin
temperatura_kelvin = float(input("Ingresa la temperatura en Kelvin: "))

# Conversión a Fahrenheit
temperatura_fahrenheit = kelvin_to_fahrenheit(temperatura_kelvin)

# Impresión del resultado
print("La temperatura en Fahrenheit es:", temperatura_fahrenheit)
