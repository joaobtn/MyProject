# Demonstração de Listas e Tuplas em Python

#Para declarar as listas, utilizamos colchetes []
#As listas são mutáveis, ou seja, podemos alterar seus elementos após a criação da lista
LISTA = []
LISTA_INTEIROS = [1, 2, 3, 4, 5]
LISTA_STRINGS = ["Python", "Java", "C++", "JavaScript"]
LISTA_MISTA = [1, "Python", 3.14, True]

# PARA DECLARAR AS TUPLAS, UTILIZAMOS PARÊNTESES ()
# As tuplas são imutáveis, ou seja, não podemos alterar seus elementos após a criação da tupla
TUPLA = ()
TUPLA_INTEIROS = (1, 2, 3, 4, 5)
TUPLA_STRINGS = ("Python", "Java", "C++", "JavaScript")
TUPLA_MISTA = (1, "Python", 3.14, True)


#PARA ACESSAR OS ELEMENTOS DA LISTA OU TUPLA, UTILIZAMOS O ÍNDICE, QUE COMEÇA EM 0
TUPLA_SEMANA = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
TUPLA_FIBONACCI = (0, 1, 1, 2, 3, 5, 8, 13, 21)

#PARA ACESSAR PS ELEMENTOS DA LISTA
print(LISTA_INTEIROS) # Imprime o primeiro elemento da lista de inteiros
print(LISTA_STRINGS[0]) # Imprime o primeiro elemento da lista de strings
print(LISTA_MISTA[1]) # Imprime o primeiro elemento da lista mista

#PARA ACESSAR OS ELEMENTOS DA TUPLA
print(TUPLA_SEMANA[2]) # Imprime o primeiro elemento da tupla de dias da semana
print(TUPLA_FIBONACCI) # Imprime o primeiro elemento da tupla de números de Fibonacci