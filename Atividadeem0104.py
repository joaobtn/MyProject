# Construa uma simples matriz 2X2 e, como saída desse programa, a média e a soma dos valores deverão ser calculadas e impressas na tela.

print("Matriz 2X2:")
MATRIZ = [[0,0],
          [0,0]]
SOMA = 0
for X in range(0, 2):
    for Y in range(0, 2):
        MATRIZ[X][Y] = int(input(f'Digite o valor da posição {X}{Y}: '))
        SOMA += MATRIZ[X][Y]

MEDIA = SOMA / 4

print("Soma dos valores:", SOMA)
print("Média dos valores:", MEDIA)