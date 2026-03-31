#Demonstração de acesso listas

print("Vou montar a marmita com 5 alimentos!")
MARMITA = ["Feijão", "Arroz", "Legumes", "Salada", "Carne"]
print("Eis, a nossa recomendação:" , MARMITA)

RESPOSTA = input("QUER MONTAR UMA MARMITA DIFERENTE (S/N)?")
if RESPOSTA == "S":
    for X in range(len(MARMITA)):
        print(f'Digite o {X+1}º item do cardápio:')
        MARMITA[X] = input()
    print("A marmita montada foi:" , MARMITA)
    print("Os 3 primeiros itens da marmita são:" , MARMITA[0:3])
    print("O ultimo item da marmita é:" , MARMITA[-1])
else:
    print("Ok, você decide...")