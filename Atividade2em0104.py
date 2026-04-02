# Construa um jogo chamado quadrado mágico, onde o usuário deverá preencher uma matriz 3X3 com números de 1 a 9, sem repetir nenhum número. O programa deverá verificar se a soma dos números em cada linha, coluna e nas diagonais é igual a 15. Se for, o programa deve imprimir "Quadrado Mágico!", caso contrário, deve imprimir "Não é um Quadrado Mágico!".
print("Bem-vindo ao jogo do Quadrado Mágico!")
QUADRADO = [[0,0,0],
            [0,0,0],
            [0,0,0]]
NUMEROS = []
for X in range(0, 3):
    for Y in range(0, 3):
        while True:
            NUMERO = int(input(f'Digite um número de 1 a 9 para a posição {X}{Y}: '))
            if NUMERO < 1 or NUMERO > 9:
                print("Número inválido! Digite um número entre 1 e 9.")
            elif NUMERO in NUMEROS:
                print("Número já utilizado! Digite um número diferente.")
            else:
                QUADRADO[X][Y] = NUMERO
                NUMEROS.append(NUMERO)
                break