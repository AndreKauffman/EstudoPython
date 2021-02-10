maior = 0
menor = 0

for c in range(1,6):
    peso = float(input("Peso da {}° pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso

print("O maior peso foi {}kg".format(maior))
print("o menor peso foi {}kg".format(menor))
