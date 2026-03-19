# Jogo de par ou impar
import random

print("Bem-vindo ao jogo de par ou impar!")
num1 = int(input("Digite um número: "))
COMPUTADOR = random.randint(1, 10)

soma = num1 + COMPUTADOR
print(f"você jogou: {num1} e o resultado do computador foi: {COMPUTADOR}. A soma é: {soma}.")

if soma % 2 == 0:
    RESULTADO = "par"
    print("O resultado é par!")
else:    
    RESULTADO = "impar"
    print("O resultado é impar!")

if RESULTADO == "par":
    print("Parabéns, você ganhou!")
else:    print("Ops, você perdeu! Tente novamente...")