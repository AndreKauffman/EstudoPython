resp = 's'
a = cont = 0
maior = menor = 1

while resp == 's':
    num = int((input("Digite um numero: ")))
    a += num
    cont += 1
    resp = str(input("Deseja continuar? [S/N]"))

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = a / cont
print("voce digitou {} valores e a media é {}".format(cont, media))
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
