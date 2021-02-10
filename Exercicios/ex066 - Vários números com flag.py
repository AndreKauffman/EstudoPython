cont = soma = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    cont+=1
    soma = soma + num
print("A soma dos {} valores é {}".format(cont, soma))
