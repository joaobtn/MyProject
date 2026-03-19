# Demonstração do uso de funções
IDADE = int(input("Digite sua idade: "))
INFANTIL = ("Bom dia e companhia, Hora de aventura, Patrulha canina")
ADULTO = ("Corsa, Onix, Gol, Uno, a partir de R$ 20.000,00")

def APRESENTAR():
    print(f"Sua idade é de {IDADE} anos.")
    if IDADE < 18:
        print(f"Assista aos seus programas favotiros como: {INFANTIL}.")
    else:
        print(f"Veja nossas opções de carros à venda: {ADULTO}.")


APRESENTAR()
