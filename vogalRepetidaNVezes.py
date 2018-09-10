palavra , num , vogal = input().split()
num = int(num)
palavra = list(palavra)

if num > 1:
    for i in range(len(palavra))[::-1]:
        if palavra[i] == vogal:
            palavra.insert( i+1, vogal)

if num <= 0:
    for i in range(len(palavra))[::-1]:
        if palavra[i] == vogal:
            del palavra[i]

print(palavra)