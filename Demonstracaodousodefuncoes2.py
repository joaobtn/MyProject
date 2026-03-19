# Demonstração do uso de funções
def ADICAO(X, Y):
    W = X + Y
    return W
def SUBTRACAO(X, Y):
    W = X - Y
    return W  

print("Digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = input("Qual operação deseja realizar? (Digite + para adição ou - para subtração): ")

if OP == "+":
    Z = ADICAO(N1, N2)
    print(f"O resultado da adição é: {Z}")
elif OP == "-":
    Z = SUBTRACAO(N1, N2)
    print(f"O resultado da subtração é: {Z}")
else:
    print("Operação inválida. Por favor, escolha + ou -.")