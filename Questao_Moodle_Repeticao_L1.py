soma  = 0
a = int(input())
b = int(input())

if b >= a:
    for a in range(a, b+1):
        soma = soma + a
    a += 1
    print(soma)
else:
    print("invalido")