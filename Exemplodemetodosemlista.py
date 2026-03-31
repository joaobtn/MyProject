# Demonstração de métodos em listas...
INSS = ["Maria", "Manoel", "José", "Isabela"]
print("Eis a fila do do INSS:", INSS)

NOVO = input("Insira mais uma pessoa: ")
INSS.append(NOVO)
print("Conferindo a nova lista", INSS)

print("Vou tirar a última pessoa desta lista...")
ESPECIAL = INSS.pop()
print("Conferindo a lista: ", INSS)

print("Agora, vou colocá-la na frente da fila...")
INSS.insert(0, ESPECIAL)
print("Conferindo a lista: ", INSS)

print("Maria não gostou e reclamou...")
INSS.remove("Maria")
print("E agora, ela saiu 'Pé da vida' ", INSS)

print("Para não ter mais reclamação, vamos atender...")
INSS.sort()
print("... em ordem alfabética: ", INSS)

print("Onde está esta nova pessoa chamada", ESPECIAL, "?")
print("Ela está na posição: ", INSS.index(ESPECIAL)+1, "!")