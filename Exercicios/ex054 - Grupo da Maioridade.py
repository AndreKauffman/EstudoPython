from datetime import date
cont = 1
a = 0
b = 0
for c in range(1, 7+1):
    idade = int(input("Em que ano a {}° pessoa nasceu? ".format(cont)))
    data = date.today().year
    soma = data - idade
    cont+=1
    if soma > 18:
        a += 1
    else:
        b += 1

print("{} são maiores de idade".format(a))
print("{} são menores de idade".format(b))
