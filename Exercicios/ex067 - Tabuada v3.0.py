while True:
    num = int(input("Digite um numero pra ver sua tabuada: "))
    print("----------------------")
    if num < 0:
        break
    for c in range(1,11):
        soma = num * c
        print("{} x {} = {}".format(num,c,soma))
    print('----------------------')