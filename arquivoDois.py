vezes =  int(input())
numMaior = int(0)

for i in range(vezes):
    num = int(input())
    if num > numMaior:
        numMaior = num

print(numMaior)
