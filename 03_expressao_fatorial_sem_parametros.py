def fatorial(x):
    fat = 1
    for i in range(2, x+1):
        fat = fat * i
    return fat

fat5 = fatorial(5)
fat4 = fatorial(4)
fat3 = fatorial(3)

E = fat5 - fat4 + fat3


print(fat3)