import random
from time import sleep
itens = ['pedra', 'papel', 'tesoura']
comp = random.randint(0,2)
print("""Suas opções:
[ 0 ] = PEDRA
[ 1 ] = PAPEL 
[ 2 ] = TESOURA""")
usuario = int(input("qual é sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-=-" *12)
print("O computador escolheu {}".format(itens[comp]))
print("O Usuario escolheu {}".format(itens[usuario]))
print("-=-" *12)

if comp == 0 and usuario == 1:
    print("Jogador vence")
elif comp == 1 and usuario == 2:
    print("Jogador vence")
elif comp == 2 and usuario == 0:
    print("Jogador vence")

elif usuario == 0 and comp == 1:
    print("Computador vence")
elif usuario == 1 and comp == 2:
    print("Computador vence")
elif usuario == 2 and comp == 0:
    print("Computador vence")

else:
    print("Empate")