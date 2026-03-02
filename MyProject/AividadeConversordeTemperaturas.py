# CONVERSÃO DE TEMPERATURAS

TEMPERATURA_CELSIUS = float(input("Digite o valor da temperatura em Celsius: "))
TEMPERATURA_KELVIN = float(input("Digite o valor da temperatura em Kelvin: "))
TEMPERATURA_FAHRENHEIT = float(input("Digite o valor da temperatura em Fahrenheit: "))

# Celsius → Kelvin e Fahrenheit
VALOR1 = TEMPERATURA_CELSIUS + 273.15
VALOR2 = (TEMPERATURA_CELSIUS * 1.8) + 32
print("O resultado de Celsius para Kelvin é:", VALOR1)
print("O resultado de Celsius para Fahrenheit é:", VALOR2)

# Kelvin → Celsius e Fahrenheit
VALOR1 = TEMPERATURA_KELVIN - 273.15
VALOR2 = (TEMPERATURA_KELVIN - 273.15) * 1.8 + 32
print("O resultado de Kelvin para Celsius é:", VALOR1)
print("O resultado de Kelvin para Fahrenheit é:", VALOR2)

# Fahrenheit → Celsius e Kelvin
VALOR1 = (TEMPERATURA_FAHRENHEIT - 32) / 1.8
VALOR2 = ((TEMPERATURA_FAHRENHEIT - 32) / 1.8) + 273.15
print("O resultado de Fahrenheit para Celsius é:", VALOR1)
print("O resultado de Fahrenheit para Kelvin é:", VALOR2)