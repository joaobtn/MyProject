# Demonstração de estrutura repetitiva...
print("Qual é o melhor clube de futbol do Brasil?")

CLUBE = 0; RESPOSTA = ""
while RESPOSTA != "Flamengo":
    print("Digite a resposta:")
    RESPOSTA = input()

    if RESPOSTA == "Flamengo":
        print("Acertou miseravi!!!")
        break
    else:
        print("Errou lazarento!")

