nome = str(input("qual é seu nome: "))
if nome == 'andre':
    print("que nome lindo!")
else:
    print("seu nome é normal!")
print("bom dia, {}!\n\n\n\n\n".format(nome))


nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite outra nota: "))
soma = (nota2 + nota1) / 2
if nota1 > 5:
    print("parabens {} voce foi aprovado com a nota {}".format(nome,soma))
else:
    print("voce foi reprovado com a nota!".format(soma))
