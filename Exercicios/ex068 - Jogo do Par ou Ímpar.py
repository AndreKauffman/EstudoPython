cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'

         }

import random
from time import sleep
print("-=" *15)
print("Vamos jogar {}Impar{} ou {}Par{}".format(cores['azul'],cores['limpa'], cores['vermelho'], cores['limpa']))
print("-=" *15)
aleatorio = random.randint(1,10)
cont = 1
vencedor = 0

while cont <=2:
    valor = int(input("Digite um valor: "))
    jogo = str(input("Impar ou Par [i/p]: "))
    soma = aleatorio + valor
    sleep(2)
    if jogo == 'i' and soma % 2 == 1:
        print("{}Jogador venceu{}".format(cores['amarelo em negrito'], cores['limpa']))
        vencedor +=1
    elif jogo == 'i' and soma % 2 == 0:
        print("{}Computador ganhou{}".format(cores['roxo em negrito'], cores['limpa']))
    elif jogo == 'p' and soma % 2 == 0:
        print("{}Jogador venceu{}".format(cores['amarelo em negrito'], cores['limpa']))
        vencedor += 1
    elif jogo == 'p' and soma % 2 == 1:
        print("{}Computador ganhou{}".format(cores['roxo em negrito'], cores['limpa']))
    print("Você jogou {}, o computador {} e o total é {}".format(valor, aleatorio, soma))
    if soma % 2 == 0:
        print('-=' * 5)
        print("Deu par")
    else:
        print('-=' * 5)
        print("Deu impar")
    if vencedor == 1:
        print('-=' * 5)
        print("Voce {}venceu{}".format(cores['azul em negrito'], cores['limpa']))
        print('-=' * 5)
    else:
        print('-=' * 5)
        print("Voce {}perdeu{}".format(cores['vermelho em negrito'], cores['limpa']))
        print('-=' * 5)
    cont+=1
    sleep(1)
print("Voce ganhou {}{}{} vezes".format(cores['roxo'],vencedor, cores['limpa']))
