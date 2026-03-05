# Demonstração do uso da estrutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
    print("Digite o número negativo para sair:")
    NUMERO = int(input())
    continue
    print("Este texto não será exibido! Mas...")
else:
    print("O número digitado foi:", NUMERO)