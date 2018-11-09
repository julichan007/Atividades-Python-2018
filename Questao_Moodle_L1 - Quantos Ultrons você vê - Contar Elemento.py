ultron, qtd = raw_input().split()
inimigos = raw_input().split()
contUltrons = 0

for inim in inimigos:
    if inim == ultron:
        contUltrons = contUltrons + 1

print contUltrons