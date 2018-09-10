#descrição
#leia 10 notas, encontre a media e diga quantas notas são maiores que a media

soma = 0
cont = 0
media = 0
for i in range(10):
    nota = float(input("Insira uma nota"))
    soma = soma + nota
   # if nota > media:
        #cont = cont + 1
media = soma / 10
print("media=: ",media)

for i in range(10):
   if nota > media: #nota possui apenas a ultima nota digitada
        cont = cont + 1


print(cont, "notas maiores que a media!")