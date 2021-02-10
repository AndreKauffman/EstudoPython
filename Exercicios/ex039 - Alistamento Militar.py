from datetime import date
data = date.today().year
idade = int(input("ano de nascimento: "))
idade1 = data - idade
alistamento = 18 - idade1
alistamento1 = alistamento * -1
ano = alistamento1 - data
ano1 = ano * -1

print("Quem nasceu em {} tem {} anos em {}".format(idade, idade1, data))
if idade1 > 18:
    print("voce deveria ter se alistado {} ano atras".format(alistamento1))
    print("seu alistamento foi em {}".format(ano1))
elif idade1 < 18:
    print("Ainda falta {} anos para o alistamento".format(alistamento))
    print("seu alistamento sera em {}".format(ano1))
else:
    print("Voce tem que se alistar imediatamente")


