# Construa um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serrão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado uma lista chamada GABARITO con as seguintes respostas: B,C,A,E,D.
GABARITO = ["B", "C", "A", "E", "D"]
ACERTOS = 0
for x in range(5):
    RESPOSTA = input("Insira a resposta da questão " + str(x+1) + ": ")
    if RESPOSTA.upper() == GABARITO[x]:
        ACERTOS += 1
else:
    print("Fim da avaliação!")

print("Quantidade de acertos:", ACERTOS)