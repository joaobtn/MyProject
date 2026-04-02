JOGADORES = []

# Cadastro dos jogadores
for i in range(11):
    nome = input("Digite o nome do jogador " + str(i+1) + ": ")
    numero = input("Digite o número da camisa do jogador " + str(i+1) + ": ")
    posicao = input("Digite a posição do jogador " + str(i+1) + ": ")
    
    JOGADORES.append([nome, numero, posicao])

print("\nEscalação dos jogadores:")
for jogador in JOGADORES:
    print(f"Nome: {jogador[0]}, Número: {jogador[1]}, Posição: {jogador[2]}")

print("\nFim da escalação!")
print("Intervalo do jogo. O técnico pode realizar substituições.")

SUBSTITUICOES = 0

while SUBSTITUICOES < 3:
    substituir = input("Deseja realizar uma substituição? (S/N): ")

    if substituir.upper() == "S":
        numero_substituir = input("Digite o número da camisa do jogador a ser substituído: ")
        
        nome_novo = input("Digite o nome do novo jogador: ")
        numero_novo = input("Digite o número da camisa do novo jogador: ")
        posicao_nova = input("Digite a posição do novo jogador: ")

        for i in range(len(JOGADORES)):
            if JOGADORES[i][1] == numero_substituir:
                JOGADORES[i] = [nome_novo, numero_novo, posicao_nova]
                SUBSTITUICOES += 1
                print(f"Substituição realizada: {numero_substituir} por {numero_novo}")
                break

    elif substituir.upper() == "N":
        break
    else:
        print("Opção inválida. Digite S ou N.")

print("\nEscalação final:")
for jogador in JOGADORES:
    print(f"Nome: {jogador[0]}, Número: {jogador[1]}, Posição: {jogador[2]}")