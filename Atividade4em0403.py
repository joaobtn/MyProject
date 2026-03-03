# Programa para exercer em um jogo de futbol...

print("Digite a posição em que deseja jogar: ")
GOLEIRO = int(input("POSIÇÃO: "))
LATERAL = int(input("POSIÇÃO: "))
ZAGUEIRO = int(input("POSIÇÃO: "))
ALA = int(input("POSIÇÃO: "))
VOLANTE = int(input("POSIÇÃO: "))
MEIA = int(input("POSIÇÃO: "))
ATACANTE = int(input("POSIÇÃO: "))
CENTROAVANTE = int(input("POSIÇÃO: "))



if GOLEIRO or ZAGUEIRO or LATERAL:
    print("Defesa!")
elif ALA or VOLANTE or MEIA:
    print("Meio-Campo")
elif ATACANTE or CENTROAVANTE:
    print("Ataque!")
else:
    print("Teimoso!")