# Programa 1 - Verificar saldo

saldo = float(input("Digite o saldo da sua conta bancária: R$ "))
valor_produto = float(input("Digite o valor do produto que deseja comprar: R$ "))

if saldo >= valor_produto:
    restante = saldo - valor_produto
    print("Compra aprovada!")
    print("Saldo restante: R$", restante)
else:
    falta = valor_produto - saldo
    print("Saldo insuficiente!")
    print("Faltam R$", (falta), "para realizar a compra.")