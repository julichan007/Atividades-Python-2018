# recebe [0 3 4 6 7 9 2 5 ] 6        #recebe vetor e numero, procurar numero
# dentro desse vetor, retornar numero com o indice que o numero foi encontrado


def encontraVetor(vetor, n):
    numvetor = 0
    procurado = int(n)
    print ("o numero procurado é: ", procurado)
    #for i in vetor:
    for i in range(len(vetor)):
        ale = int(vetor[i])

        if procurado == ale:
            numvetor = i
    return numvetor



lista, num = input().split()
num = int(num)
#lista = lista.split(" ")
print(lista, num)

print(encontraVetor(lista, num))

