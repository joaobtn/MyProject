def verificar_cidade(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        print(f"{nome}, Seja Bem-vindo à Cidade Maravilhosa!")
    else:
        print(f"Nome: {nome}")
        print(f"Cidade: {cidade}")

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

verificar_cidade(nome, cidade)