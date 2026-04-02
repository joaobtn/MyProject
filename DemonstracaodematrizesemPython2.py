# Demonstração em matrizes em Python...

print("Eis, o teclado númerico do terminal:")
TECLADO = [["1","2","3"],
          ["4","5","6"],
          ["7","8","9"],
            ["*","0","#"]]
SENHA = []

print("Digite a senha de 4 dígitos:")
for X in range(0, 4):
    SENHA.append(input(f'Digite o dígito {X+1}: '))

for X in range(0, 4):
    for Y in range(0, 3):
        for Z in range(0, 4):
            if TECLADO[X][Y] == SENHA[Z]:
                TECLADO[X][Y] = "X"

print("Eis, a senha digitada:", SENHA)
print("Confira, as teclas pressionadas:")
for TECLA in TECLADO:
    print(TECLA)