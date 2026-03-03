# Demonstração de condicionais e operadores....
TEMPO = input("Qual a condição meteorológica?")
RESERVA = input("Tem algum dinheiro na conta?")

if TEMPO == "sol" and RESERVA == "sim":
    print("Dá pra ir à praia!")

if not TEMPO == "sol" and RESERVA =="sim":
    print("Comprar pizza e assistir Netflix")
          
if TEMPO == "sol" and RESERVA == "não":
    print("Vamos passear de bicicleta!")