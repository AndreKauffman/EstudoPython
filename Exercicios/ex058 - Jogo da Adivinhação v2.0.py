import random
aleatorio = random.randint(0,10)

print("Sou seu computador, acabei de pensar em um numero de 0 a 10.")
print("Consegue advinhar? ")

palpite = int(input("Qual seu palpite: "))
cont = 0

while palpite != aleatorio:
    if aleatorio > palpite:
        palpite = int(input("Mais... Tente novamente..."))
        cont += 1
    else:
        palpite = int(input("Menos... Tente novamente"))
        cont += 1
print("Voce acertou e demorou {} vezes".format(cont+1))