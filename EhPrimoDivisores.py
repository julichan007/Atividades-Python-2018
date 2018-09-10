#retorna o numero de divisores de x
def divisores( x ):
    cont = 0
    for candidato in range(1,x+1):
        if x%candidato==0:
            cont += 1
    return cont
#retorna se p eh ou nao eh primo
def primo( p ):
    nDivP = divisores( p )
    if nDivP == 2:
        return True
    else:
        return False

print(divisores(9))