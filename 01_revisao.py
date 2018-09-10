# retorna o numero de divisores de x
def divisores(x):
    cont = 0
    for candidato in range(1, x + 1):
        if x % candidato == 0:
            cont += 1
    return cont


# retorna se p eh ou nao eh primo
def primo(p):
    nDivP = divisores(p)
    if nDivP == 2:
        return True
    else:
        return False


# n = int(input("Insira um numero: "))
# if ( primo(n) ):
#    print "Eh primo!"
# else:
#    print "Nao eh primo!"

# multiplique todos os primos entre 70 e 90
mult = 1
for i in range(70, 91):
    if primo(i):
        mult = mult * i

print ("Mult =", mult)
print (71 * 73 * 79 * 83 * 89)

print (divisores(9))
