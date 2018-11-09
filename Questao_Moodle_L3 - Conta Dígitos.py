digitoProcurado = int(input())
numerodeContato = int(input())
cont = 0

for i in range(0, 8):
    digito = numerodeContato % 10
    if digito == digitoProcurado:
        cont = cont + 1
    numerodeContato = numerodeContato / 10

print(cont)