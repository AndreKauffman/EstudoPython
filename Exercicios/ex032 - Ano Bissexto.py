from datetime import date
ano = int(input("Qual ano quer analizar? Digite 0 para analizar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("o ano {} não é Bissexto".format(ano))