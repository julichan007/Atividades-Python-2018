#descrição
#leia 10 notas, encontre a media e diga quantas notas são maiores que 4

soma = 0
cont = 0
for i in range(10):
    nota = float(input("Insira uma nota"))
    soma = soma + nota
    if nota > 4:
        cont = cont + 1
media = soma / 10

print("media=: ",media)
print(cont, "notas maiores que 4!")