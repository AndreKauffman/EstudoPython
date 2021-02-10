num = int(input("Digite um numero [999 para parar] "))
cont = 0
a = 0
while num != 999:
    a = a + num
    num = int(input("Digite um numero [999 para parar] "))
    cont+=1
print("Voce digitou {} numeros e a soma deles é {}".format(cont, a))