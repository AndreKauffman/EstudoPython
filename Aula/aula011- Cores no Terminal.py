
    # Style : 0 = null
    #         1 = null
    #         4 = sublinhado em baixo
    #         7 = inverte o fundo e a letra


    # Text : 30 = branco
    #        31 = vermelho
    #        32 = verde
    #        33 = amarelo
    #        34 = azul claro
    #        35 = roxo
    #        36 = azul
    #        37 = cinza


    # Back : 30 = branco
    #        31 = vermelho
    #        32 = verde
    #        33 = amarelo
    #        34 = azul claro
    #        35 = roxo
    #        36 = azul
    #        37 = cinza


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
nome = 'Andre'
print("Olá, muito pra zer em te conhecer {}{}{}!!!".format(cores['vermelho em negrito'], nome, cores['limpa']))


