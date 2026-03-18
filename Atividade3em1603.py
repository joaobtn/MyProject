numeros = []

print("Digite 6 números diferentes para jogar na Mega-Sena")

while len(numeros) < 6:
    numero = int(input(f"Digite o {len(numeros)+1}º número: "))

    if numero in numeros:
        print("Número repetido! Digite um número diferente.")
    else:
        numeros.append(numero)

print("\nNúmeros escolhidos:", numeros)
