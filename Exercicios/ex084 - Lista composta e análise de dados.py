resp = 's'
nomes = []
dados = []
peso = []
cont = 0
while resp == 's':
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    nomes.append(dados[:])
    peso.append(dados[1])
    cont+=1
    dados.clear()
    resp = str(input("Deseja continuar? [S/N]: "))
print(f"Ao todo voce cadastrou {cont} pessoas...")
print(f"O maior peso foi {max(peso)}kg de", end=' ')
for p in nomes:
    if p[1] == max(peso) or p[1] == peso:
        print(p[0], end=' ')
print(f"O menor peso foi {min(peso)}kg de", end=' ')
for p in nomes:
    if p[1] == min(peso) or p[1] == peso:
        print(p[0], end=' ')

