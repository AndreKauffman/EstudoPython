sexo = str(input("Digite seu sexo [F/M]: ")).strip().upper()[0]
while sexo not in 'fmFM':
    sexo = str(input("Digite o valor correto! ")).strip().upper()[0]
print("Sexo {} cadastrado com sucesso!".format(sexo))