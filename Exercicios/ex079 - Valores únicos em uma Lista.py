valores = []
resp = 's'
while resp == 's':
    num = int(input("Digite um numero: "))
    if num in valores:
        print("Valor duplicado, não será adicionado! ")
    else:
        valores.append(num)
        print("Valor Adicionado com sucesso!")
    resp = str(input("Quer continuar? S/N: "))
print('=' * 30)
valores.sort()
print("Voce digitou os valores {} ".format(valores))
