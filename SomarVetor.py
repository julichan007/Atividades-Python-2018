valores = input().split()
soma = 0

for i in range(1, int(valores[0])+1):
    soma = soma + int(valores[i])

print (soma)