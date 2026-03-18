# Programa para calcular o fatorial de um número entre 0 e 25

numero = int(input("Digite um número entre 0 e 25: "))

# Validação do valor
if numero < 0 or numero > 25:
    print("Valor inválido! Digite um número entre 0 e 25.")
else:
    fatorial = 1
    
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    
    print("O fatorial de", numero, "é:", fatorial)