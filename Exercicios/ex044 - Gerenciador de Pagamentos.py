print("========== ANDRÉ MARKET =========")
preco = float(input("Digite o preço: "))
print("""FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO
[ 2 ] À VISTA CARTÃO
[ 3 ] 2X CARTÃO
[ 4 ] 3X OU MAIS
""")

forma = float(input("Qual a forma? "))

if forma == 1:
    preco1 = preco * 10 / 100
    preco2 = preco - preco1
    print("o produto custa R${}, a vista ira custar R${}".format(preco, preco2))
elif forma == 2:
    preco1 = preco * 5 / 100
    preco2 = preco - preco1
    print("o produto custa R${}, a vista no cartão ira custar R${}".format(preco, preco2))
elif forma == 3:
    preco1 = preco / 2
    print("Irá pagar duas parcelas de R${}".format(preco1))
elif forma == 4:

    parcelas = float(input("quantas parcelas? "))

    preco1 = preco * 20 / 100
    preco2 = preco + preco1
    preco3 = preco2 / parcelas

    print("Sua compra sera parcelada em {:.0f}X de R${} COM JUROS".format(parcelas, preco3))
    print("Sua compra de R${} vai custar R${}".format(preco, preco2))