import random
from time import sleep
from operator import itemgetter
dado = {}
print('-' *30)
print("Valores Sorteados: ")
sleep(0.8)

dado = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}

ranking = {}
for k,v in dado.items():
    print(f"{k} jogou e o dado caiu com o valor: {v}")
    sleep(0.8)
print('-' * 30)
print(" == " 'RANKING DOS JOGADORES'' == '"")
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}. ')
    sleep(0.8)

