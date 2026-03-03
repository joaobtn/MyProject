# Programa de avaliação de filme ou série

nome = input("Digite o nome do filme ou série: ")

nota = int(input("Dê uma nota de 1 a 5: "))

if nota == 1:
        print("Péssimo")
        motivo = input("Que pena! Poderia descrever por que avaliou de forma negativa? ")
        print("Obrigado pelo seu feedback!")

elif nota == 2:
        print("Ruim")
        motivo = input("Que pena! Poderia descrever por que avaliou de forma negativa? ")
        print("Obrigado pelo seu feedback!")

elif nota == 3:
        print("Razoável")

elif nota == 4:
        print("Bom")

elif nota == 5:
        print("Ótimo")

else:
        print("Alerta: Nota inválida! Digite um valor entre 1 e 5.")
