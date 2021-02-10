print('-' *30)
print("LOJA SUPER BARATÂO")
print('-' *30)
resp = 's'
menor = 'andre'
contpreco = menor1 = a = 0
cont = 0
while True:
    if resp == 'n':
        break
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Preço R$ "))
    resp = str(input("Deseja continuar: [S/N]"))
    cont+=1
    a+=preco

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            menor1 = nome

    if preco > 1000:
        contpreco +=1

print("------- FIM -------")
print("O preço total de compras foi de R${:.2f}".format(a))
print("Temos {} produtos custando mais de R$ 1000,00".format(contpreco))
print("O produto mais batato foi {} que custou R${:.2f}".format(menor1, menor))