valores = []
impar = []
par = []
resp = 's'
while resp == 's':
    num = int(input("Digite um valor: "))
    valores.append(num)
    print("Valor Adicionado com sucesso!")
    resp = str(input("Quer continuar? S/N: "))

for num in valores:
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)

print('=' * 30)
print("A lista completa é {}".format(valores))
print("A lista de pares é {}".format(par))
print("A lista de impares é {}".format(impar))
