SAQUE = int(input("Digite o valor do saque: "))

CEDULA200 = 0
CEDULA100 = 0
CEDULA50 = 0
CEDULA20 = 0
CEDULA10 = 0
CEDULA5 = 0
CEDULA2 = 0

while SAQUE >= 200:
    CEDULA200 += 1
    SAQUE = SAQUE - 200
    
while SAQUE >= 100:
    CEDULA100 += 1
    SAQUE = SAQUE - 100 

while SAQUE >= 50:
    CEDULA50 += 1
    SAQUE = SAQUE - 50  

while SAQUE >= 20:
    CEDULA20 += 1
    SAQUE = SAQUE - 20

while SAQUE >= 10:
    CEDULA10 += 10
    SAQUE = SAQUE - 10

while SAQUE >= 5:
    CEDULA5 += 1
    SAQUE = SAQUE - 5

while SAQUE >= 2:
    CEDULA2 += 1
    SAQUE = SAQUE - 2

print("Cédulas entregues:")
print("200:", CEDULA200)
print("100:", CEDULA100)
print("50:", CEDULA50)
print("20:", CEDULA20)
print("10:", CEDULA10)
print("5:", CEDULA5)
print("2:", CEDULA2)


