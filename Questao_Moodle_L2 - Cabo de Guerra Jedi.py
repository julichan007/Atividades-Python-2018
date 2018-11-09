lista = []
jedi = 0
sith = 0
p = 0
ver = True
a = int(input())
if ver == True:
    if a %2 !=0:
        print("Tamanho invalido! Somente valores pares!")
    if a > 50 or a < 0:
        print("Tamanho invalido! Somente valores entre 0 e 50!")
        p +=1

    else:
        b = raw_input().split()
        for i in range(a):
            if int(b[i]) > 10 or int(b[i]) < 1:
                print("Valores de vetor invalido! Somente valores entre 1 e 10!")
                p += 1
            else:
                lista.append(int(b[i]))
    mid = a//2

if p == 0:
    for i in range(mid):
        jedi += lista[i]
    for i in range(mid,len(lista)):
        sith += lista[i]

    if jedi > sith:
        print("Jedi!")
    elif jedi < sith:
        print("Sith!")
    elif jedi == sith:
        print("Empate!")