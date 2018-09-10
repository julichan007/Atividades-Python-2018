#leia n valores e mostre o maximo e o minimo
n = int(input())
minimo = 999999
maximo = - 999999

for i in range(n):
    valor= int(input())
    if valor < minimo:
        minimo =  valor
    if valor > maximo:
        maximo = valor

print(maximo + minimo)
