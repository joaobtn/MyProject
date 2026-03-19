# Resolução do problema do caixa eletrônico
SAQUE = int(input("Digite o valor do saque: "))

CONT50 = 0
CONT20 = 0
CONT10 = 0

while True:
    if SAQUE >= 50:
        CONT50 += 1
        SAQUE = SAQUE - 50
    elif SAQUE >= 20:
        CONT20 += 1
        SAQUE = SAQUE - 20
    elif SAQUE >= 10:
        CONT10 += 1
        SAQUE = SAQUE - 10
    else:
        break

if SAQUE != 0:
    print("Valor restante não pode ser sacado:", SAQUE)

print("Cédulas:")
print("50:", CONT50)
print("20:", CONT20)
print("10:", CONT10)