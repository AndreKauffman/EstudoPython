from time import sleep
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
menu = 0
maior = 0
while menu != 5:

    print("""        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] SAIR""")
    menu = int(input(" >>>>>>> Qual sua opção? "))

    if menu == 1:
        num3 = num1 + num2
        print("A soma entre {} e {} é {}".format( num1, num2,num3))
        print('-=' * 5)
        sleep(4)
    elif menu == 2:
        num3 = num1 * num2
        print("A multiplicação entre {} X {} é {}".format(num1, num2, num3))
        print('-=' * 5)
        sleep(4)
    elif menu == 3:
        if num1 > num2:
            maior = num1
            print("Entre {} e {} o numero {} é maior".format(num1, num2, maior))
            print('-=' * 5)
            sleep(4)
        else:
            maior = num2
            print("Entre {} e {} o numero {} é maior".format(num1, num2, maior))
            print('-=' * 5)
            sleep(4)
    elif menu == 4:
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))

print("Fim")
