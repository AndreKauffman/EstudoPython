valor = float(input("Valor da casa: "))
salario = float(input("salario do comprador: "))
anos = float(input("quantos anos de financiamento: "))

soma = ( anos * 12 )
soma1 = valor / soma
soma2 = salario * 30 / 100

if salario > soma2:
    print("Para pagar umas casa de R${} em {} anos a prestação será de {:.2f}.".format(valor, anos, soma1))
    print("Emprestimo pode ser concedido!")
elif salario < soma2:
    print("Para pagar umas casa de R${} em {} anos a prestação será de {}.")
    print("Emprestimo negado!")
