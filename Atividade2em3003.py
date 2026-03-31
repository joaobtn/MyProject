# Construa um programa que receba a escalação dos 11 jogadores titulares que irão iniciar uma partida, registrando seus nomes e o número da camisa, além de imprimir a lista após a sua digitação. Durante o intervalo do jogo, ofereça ao técnico a opção de realizar a substituição de 3 jogadores, exibindo a lista atualizada com os respectivos nomes e números.
JOGADORES = []
for i in range(11):
    NOME = input("Digite o nome do jogador " + str(i+1) + ": ")
    NUMERO = input("Digite o número da camisa do jogador " + str(i+1) + ": ")
    JOGADORES.append((NOME, NUMERO))

print("Escalação dos jogadores:")
for jogador in JOGADORES:
    print(f"Nome: {jogador[0]}, Número: {jogador[1]}")
print("Fim da escalação!")
print("Intervalo do jogo. O técnico pode realizar substituições.")
SUBSTITUICOES = 0
while SUBSTITUICOES < 3:
    SUBSTITUIR = input("Deseja realizar uma substituição? (S/N): ")
    if SUBSTITUIR.upper() == "S":
        NUMERO_SUBSTITUIR = input("Digite o número da camisa do jogador a ser substituído: ")
        NUMERO_NOVO = input("Digite o número da camisa do novo jogador: ")
        NOME_NOVO = input("Digite o nome do novo jogador: ")
        for i in range(len(JOGADORES)):
            if JOGADORES[i][1] == NUMERO_SUBSTITUIR:
                JOGADORES[i] = (NOME_NOVO, NUMERO_NOVO)
                SUBSTITUICOES += 1
                print(f"Substituição realizada: {NUMERO_SUBSTITUIR} por {NUMERO_NOVO}")
                break
    elif SUBSTITUIR.upper() == "N":
        break
    else:
        print("Opção inválida. Por favor, digite S ou N.")