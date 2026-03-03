# Programa de recomendação baseado no dia da semana

dia = input("Digite um dia da semana: ").strip().lower()

if dia == "":
    print("⚠️ Alerta: Você não digitou nada!")

elif dia == "segunda":
    print("Que tal organizar sua semana e planejar seus objetivos?")

elif dia == "terça":
    print("Dia ideal para focar nos estudos ou trabalho!")

elif dia == "quarta":
    print("Que tal assistir um filme ou série para relaxar?")

elif dia == "quinta":
    print("Bom dia para praticar exercícios físicos!")

elif dia == "sexta":
    print("Sexta-feira! Que tal sair com amigos ou pedir algo especial?")

elif dia == "sábado":
    print("Aproveite para lazer, passeios ou hobbies!")

elif dia == "domingo":
    print("Dia perfeito para descansar e recarregar as energias!")

else:
    print("⚠️ Alerta: Dia da semana inválido!")