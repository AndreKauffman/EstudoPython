num1 = int(input("Digite um numero: "))
cont = 0
for c in range(1,num1 + 1):
    if num1 % c == 0:
        print("\033[33m", end=' ')
        cont += 1
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end=' ')
print("\n\033[mO numero {} foi dividido {} vezes".format(num1, cont))
if cont <= 2:
    print("é um numero primo!")
else:
    print("Não é um numeor primo, pois foi dividido {} vezes".format(cont))
