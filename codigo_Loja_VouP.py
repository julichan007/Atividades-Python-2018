valorTotal = int(0)
valorTotalV = int(0)
valorTotalP = int(0)
valoraprazo = int(0)
cont = 0

while cont <= 15:
    codigo = str(input())
    if codigo == "V":
        cont = cont + 1
        valorTotalV += 1
    if codigo == "P":
        cont = cont + 1
        valorTotalP += 1
valorTotal = valorTotalV + valorTotalP

print(valorTotalV)
print(valorTotalP)
print(valorTotal)




