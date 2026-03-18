# Cadastro de paciente

# Cadastro inicial
nome = input("Nome: ")
data_nascimento = input("Data de nascimento: ")
sexo = input("Sexo: ")
diagnostico = input("Diagnóstico: ")
estado = input("Estado: ")
tratamento = input("Tratamento: ")
data_liberacao = input("Data de liberação: ")

# Exibição da ficha
print("\n--- Ficha do Paciente ---")
print("Nome:", nome)
print("Data de Nascimento:", data_nascimento)
print("Sexo:", sexo)
print("Diagnóstico:", diagnostico)
print("Estado:", estado)
print("Tratamento:", tratamento)
print("Data de Liberação:", data_liberacao)

# Pergunta se deseja alterar dados
opcao = input("\nDeseja alterar os dados? (s/n): ")

if opcao.lower() == "s":
    nome = input("Novo nome: ")
    data_nascimento = input("Nova data de nascimento: ")
    sexo = input("Novo sexo: ")
    diagnostico = input("Novo diagnóstico: ")
    estado = input("Novo estado: ")
    tratamento = input("Novo tratamento: ")
    data_liberacao = input("Nova data de liberação: ")

# Ficha atualizada
print("\n--- Ficha Atualizada do Paciente ---")
print("Nome:", nome)
print("Data de Nascimento:", data_nascimento)
print("Sexo:", sexo)
print("Diagnóstico:", diagnostico)
print("Estado:", estado)
print("Tratamento:", tratamento)
print("Data de Liberação:", data_liberacao)