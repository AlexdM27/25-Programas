def base10_to_base8(number):
    if number == 0:
        return '0'
    
    result = ''
    
    while number > 0:
        remainder = number % 8
        result = str(remainder) + result
        number = number // 8
    
    return result

# Ejemplo de uso
decimal_number = 123
base8_number = base10_to_base8(decimal_number)
print("Número en base 10:", decimal_number)
print("Número en base 8:", base8_number)
