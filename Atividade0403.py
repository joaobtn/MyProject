TIME = input("Qual é o seu time? ")
POSICAO = int(input("Digite a posição do seu time: "))

if POSICAO == 1:
    print("Campeão!")
elif 2 <= POSICAO <= 6:
    print("Libertadores!")
elif 7 <= POSICAO <= 12:
    print("Sul-Americana!")
elif 13 <= POSICAO <= 16:
    print("Rebaixado!")
else:
    print("Informe uma opção válida")