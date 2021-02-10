mulher = 0
a = 0
cont = 0

for c in range(1,5):
    print("----- {}° PESSOA -----".format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo M/F: "))
    a = a + idade
    soma = a / c
    if idade < 20 and sexo == 'f' or sexo == 'F':
        mulher += 1
    if sexo in 'Mm':
        velho = idade
        if idade > velho:
            velho = idade
        if velho == idade and sexo =='m':
            nomevelho = nome

print("A media da idade do grupo é de {}".format(soma))
print("O homem mais velho tem {} anos e se chama {}".format(velho, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulher))