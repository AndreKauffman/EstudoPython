print("="*20)
print("     BANCO ANDRÉ    ")
print("="*20)
valor = int(input("Qual valor voce deseja sacar? R$ "))
cinquenta = 50
dez = 10
cinco = 5
cont = cont50 = cont10 = cont5 = 0
while valor != 0:
        if valor >= cinquenta:
            soma = valor - cinquenta
            valor = soma
            cont50 += 1
        else:
            if valor >= dez and valor < 50:
                soma = valor - dez
                valor = soma
                cont10+=1
            else:
                if valor >= 5 and valor < 10:
                    soma = valor - cinco
                    valor = soma
                    cont5 +=1
                else:
                    if valor > 0 and valor < 5:
                        soma = valor - 1
                        valor = soma
                        cont += 1

print("Foi usado {} notas de R$50,00".format(cont50))
print("Foi usado {} notas de R$10,00".format(cont10))
print("Foi usado {} notas de R$5,00".format(cont5))
print("Foi usado {} moedas de R$1,00".format(cont))