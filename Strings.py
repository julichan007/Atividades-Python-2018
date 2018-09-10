ch = input()

if ord(ch)>= ord("A") and ord(ch) <= ord("Z"):
    d = ord(ch) - ord("A")
    aux = ord("a") + d
    print(chr(aux))
else:
    d = ord(ch) - ord("a")
    aux = ord("A") + d
    print(chr(aux))