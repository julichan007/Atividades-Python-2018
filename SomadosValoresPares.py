a = int(input("Insira a: "))
b = int (input("Insira b: "))

soma = 0

for i in range(a, b+1):
    if i % 2 == 0:
        soma = soma + i

print("soma=", soma)