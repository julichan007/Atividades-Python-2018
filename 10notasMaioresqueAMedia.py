soma = 0.0
cont = 0
media = 0

#nota = [0, 0, 0, 0, 0, 0]
#indica  = endereço local para acessar as informações individuais
 nota = [0] * 10
 print nota


for i in range(10):
    nota[i] = float (input("Insira a nota:"))
    soma = soma + nota [i]

media / 10
print ("Media: ", media)

for i in range(10):
    if nota[i] > media:
        cont = cont + 1

print (cont, "notas são maiores que a media!")
