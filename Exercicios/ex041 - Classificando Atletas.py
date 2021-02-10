from datetime import date
data = date.today().year
idade = int(input("digite o ano de nascimento: "))
idade1 = data - idade

print("o atleta tem {} anos".format(idade1))
if idade1 <= 10:
    print("Classificação: MIRIM ")
elif idade1 <= 20:
    print("Classificação: JUNIOR ")
elif idade1 <= 35:
    print("Classificação: SENIOR ")
elif idade1 <= 50:
    print("Classificação: PLENO ")
else:
    print("Classificação: TITAN ")