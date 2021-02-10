jogador = {}
jogador1 = list()
total = 0
jogador["nome"] = str(input("Digite o nome do jogador: "))
jogador["partidas"] = int(input("Quantas partidas: "))
for c in range(1, jogador["partidas"]+1):
    jogador1.append(int(input("Quantos gols na partida {}? ".format(c))))
    jogador['gols'] = jogador1[:]
    jogador['total'] = sum(jogador1)
print('-' *30)
print(jogador)
print('-' *30)
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print('-' *30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas...')
for i, w in enumerate(jogador["gols"]):
    print(f'    => Na partida {i + 1}, fez {w} gols ')
print(f'O total foi {jogador["total"]}')
