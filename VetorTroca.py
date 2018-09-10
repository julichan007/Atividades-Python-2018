qnt = int(input())
vetor= input().split()
k = qtd =1
for i in range(0, qnt):
    aux = vetor[i]
    vetor[i] = vetor[k]
    vetor[k] = aux
    k -=1

print (vetor)
