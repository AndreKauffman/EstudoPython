valores = []
resp = 's'
cont = 0
while resp == 's':
    num = int(input("Digite um numero: "))
    valores.append(num)
    print("Valor Adicionado com sucesso!")
    cont+=1
    resp = str(input("Quer continuar? S/N: "))
print('=' * 30)
valores.sort(reverse=True)
print("Voce digitou {} elementos".format(cont))
print("Voce digitou os valores {} ".format(valores))
if 5 in valores:
    print("O valor 5 faz parte da lista...")
else:
    print("O valor 5 não faz parte da lista...")