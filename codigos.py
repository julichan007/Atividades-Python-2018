nome = input()
codigo = int(input())

if codigo >=1 and  codigo <= 5:
    print ("%s Região Nordeste" %nome)
elif codigo >= 6 and codigo <= 12:
    print( "%s Regiao NOrte"  %nome)
elif codigo >= 13 and codigo <= 16:
    print ("Regiao Sudeste"%nome)
elif codigo >= 17 and  codigo<= 22:
    print ("%s Regiao Centro Oeste" %nome)
else:
    print ("%s Regiao Sul" %nome)
