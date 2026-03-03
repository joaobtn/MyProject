# Eis, as condições para o estudante ser aprovado:
# NOTA: Igual ou acima de 6; presença igual ou acima de 75%
# Se uma das condições não forem satisfeitas, recuperação.
# Se nenhuma das condições não forem satisfeitas, reprovado.
NOTA = int(input("Digite a nota: "))
PRESENCA = int(input("Digite a presença: "))

if NOTA >= 6 and PRESENCA >= 75:
    print("Aprovado!")
elif NOTA < 6 and PRESENCA < 75:
    print("Reprovado!")
else:
    print("Recuperação")