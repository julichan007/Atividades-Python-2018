valortotal = int(0)
pedido = int(-1)

while pedido != 0:
    print("1 - Acrecenta 1/n 2 - Acrecenta 2 /n 3 - Acrecenta 3 /n 4 -Acrecenta 4 /n 5 - Acrecenta 5 /n 0 - Sair")
    pedido = int(input())
    if pedido == "1":
        valortotal  = valortotal + 1
    if pedido == "2":
        valortotal = valortotal + 2
    if pedido == "3":
        valortotal = valortotal + 3
    if pedido == "4":
        valortotal = valortotal + 4
    if pedido == "5":
        valortotal = valortotal + 5

print (valortotal)