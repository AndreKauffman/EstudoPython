galera = []
dados = []
maior = menor =  0
for c in range(1,6):
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite sua idade ")))
    galera.append(dados[:])
    dados.clear()
for dado in galera:
    if dado[1] >= 21:
        maior += 1
    else:
        menor += 1

print(f"temos {maior} maiores de idade e {menor} menores de idade")
