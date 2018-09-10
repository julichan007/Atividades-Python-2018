palavraStr = ""
for i in range(8):
    palavraStr += tabela[int(palavra[i])]
print(palavraStr)


palavra = raw_input("Insira o codigo: ")
tam = len(palavra)
print(tam)

palavraStr = ""
for i in range(tam):
    palavraStr += tabela[int(palavra[i])]
print (palavraStr)