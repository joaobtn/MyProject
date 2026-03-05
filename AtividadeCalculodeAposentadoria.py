# Cálculo de aposentadoria...
IDADE = int(input("Qual é a idade: "))
INSS = int(input("Quantos anos de contribuição: "))
INSALUBRE = int(input("Em condição insalubre (S/N)? "))

if INSALUBRE == "S":
    if INSS >= 25:
        print("Aposentadoria especial!")
    else:
        print(f"faltam {25 - INSS} anos de se aposentar...")
else:
    if IDADE >= 65 and INSS >= 35:
        print("Aposentadoria normal.")
    else:
        print("Falta atender aos requisitos...")