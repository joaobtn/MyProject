# Programa 3 - Cálculo do IMC

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc > 25:
    print("Acima do peso ideal")
elif imc < 18:
    print("Abaixo do peso ideal")
else:
    print("O seu peso está OK")