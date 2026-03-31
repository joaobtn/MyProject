# Construa um programa que permita a criação de uma lista de afazeres, totalizando a descrição de 5 tarefas diferentes. A seguir, o programa irá perguntar se a primeira tarefa já foi executada. Se sim, o programa deverá excluíla, além de dar a opção de cadastrar uma nova tarefa.
AFAZERES = []
for i in range(5):
    TAREFA = input("Digite a descrição da tarefa " + str(i+1) + ": ")
    AFAZERES.append(TAREFA)

print("Lista de afazeres:")
for tarefa in AFAZERES:
    print(f"- {tarefa}")

PRIMEIRA_TAREFA_EXECUTADA = input("A primeira tarefa já foi executada? (S/N): ")
if PRIMEIRA_TAREFA_EXECUTADA.upper() == "S":
    AFAZERES.pop(0)
    print("Primeira tarefa excluída.")
    NOVA_TAREFA = input("Digite a descrição da nova tarefa: ")
    AFAZERES.append(NOVA_TAREFA)
    print("Nova tarefa cadastrada.")

print("Lista atualizada de afazeres:")
for tarefa in AFAZERES:
    print(f"- {tarefa}")