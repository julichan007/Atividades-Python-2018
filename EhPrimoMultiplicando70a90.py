def primo(x):
    if x != 1:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else:
        return False

multi = 1
for i in range(70,90):
    if primo(i):
        multi = multi * i
        print(i)

print("multi:", multi)