# Desafio: Meu clube do coração!

print("=== Meu Clube do Coração! ===")

naturalidade = input("Você é carioca, paulista ou mineiro? ").strip().lower()

# Primeiro usamos if/elif/else para definir a lista de clubes
if naturalidade == "carioca":
    clubes = ["Flamengo", "Fluminense", "Vasco", "Botafogo"]
elif naturalidade == "paulista":
    clubes = ["Corinthians", "Palmeiras", "São Paulo", "Santos"]
elif naturalidade == "mineiro":
    clubes = ["Atlético-MG", "Cruzeiro", "América-MG"]
else:
    clubes = []

# Verifica se a naturalidade é válida
if clubes:
    print("\nTimes da sua região:")
    for time in clubes:
        print("-", time)

    voto = input("\nDigite o nome do seu clube do coração: ").strip()

    # Agora usamos match/case para personalizar a mensagem
    match voto:
        case "Flamengo":
            print("Saudações rubro-negras! 🔴⚫")
        case "Fluminense":
            print("Saudações tricolores! 🇭🇺")
        case "Vasco":
            print("A cruz de malta te acompanha! ⚫⚪")
        case "Botafogo":
            print("Glorioso! ⭐")
        case "Corinthians":
            print("Vai, Corinthians! ⚫⚪")
        case "Palmeiras":
            print("Avanti Palestra! 🟢")
        case "São Paulo":
            print("Salve o Tricolor Paulista! 🔴⚪⚫")
        case "Santos":
            print("Peixe sempre vivo! ⚪⚫")
        case "Atlético-MG":
            print("Galo forte e vingador! 🖤🤍")
        case "Cruzeiro":
            print("Zêrooo! Cabuloso! 🔵")
        case "América-MG":
            print("Coelhão na área! 🟢")
        case _:
            print("Hmm... esse time não estava na lista, mas respeitamos sua escolha 😉")

else:
    print("\nNaturalidade inválida. Execute o programa novamente e escolha entre carioca, paulista ou mineiro.")