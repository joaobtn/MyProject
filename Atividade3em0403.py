# Programa com 3 números distintos...
print("Digite o tamanho de cada lado do triângulo nas opções a seguir: ")
X = int(input("Digite o tamanho: "))
Y = int(input("Digite o tamanho: "))
Z = int(input("Digite o tamanho: "))

if X == Y and Y == Z and Z == X:
    print("Lados equiláteros!")
elif Z == Y or Y == X or Z == X:
    print("Lados Isóceles")
else:
    print("Lados escaleno")