def primo(x):
    if x != 1:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else:
        return False

for i in range(70,91):
    if (primo(i)):
        print(i)
