# Atividade
tipo = input("Qual o tipo do veículo? (carro, caminhao, moto): ")
hora = int(input("Que horas são? (digite apenas o número de 0 a 23): "))
oficial = input("É veículo oficial (polícia/ambulância)? (sim/nao): ")

#Definir o valor base
if tipo == "carro":
    valor_base = 10
elif tipo == "caminhao":
    eixos = int(input("Quantos eixos tem o caminhão? "))
    valor_base = 15 * eixos
elif tipo == "moto":
    valor_base = 5
else:
    valor_base = 0

#Verificar se é isento (oficial)
if oficial == "sim":
    valor_final = 0
else:
    #Ver se está no horário de pico
    # Pico 1: entre 6 e 9 | Pico 2: entre 17 e 20
    no_pico = (hora >= 6 and hora <= 9) or (hora >= 17 and hora <= 20)
    
    if no_pico:
        valor_final = valor_base + (valor_base * 0.20) # Adiciona 20%
    else:
        valor_final = valor_base
        
print("--------------------------")
print("Tipo de veículo:", tipo)
print("Valor a pagar: R$", valor_final)