# Programa com 3 números distintos...
X = int(input("Digite um número: "))
Y = int(input("Digite um número: "))
Z = int(input("Digite um número: "))

if X < Y and Y < Z:
    print("Ordem crescente")
elif Z < Y and Y < X:
    print("Ordem decrescente")
else:
    print("Eles estão misturados")