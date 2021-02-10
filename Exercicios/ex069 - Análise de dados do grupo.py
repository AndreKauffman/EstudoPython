resp = 's'
a = cont = contdade = mulheres = 0
while True:
    if resp == 'n':
        break
    print("=" * 25)
    print("CADASTRE UMA PESSOA")
    print("=" * 25)
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [F/M]: "))
    print("=" * 25)
    resp = str(input("Deseja continuar? [S/N]"))
    if sexo == 'm':
        cont+=1
    if idade > 18 :
        contdade+=1
    if sexo == 'f' and idade < 20:
        mulheres+=1

print("Total de pessoas com mais de 18 anos: {}".format(contdade))
print("Há {} homens cadastrados".format(cont))
print("Há {} mulheres com menos de 20 anos".format(mulheres))

