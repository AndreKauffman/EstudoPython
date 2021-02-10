time = list()
jogador = {}
jogador1 = list()
total = 0
resp = 's'
while True:
    jogador.clear()
    jogador1.clear()
    if resp == 'n':
        break
    jogador["nome"] = str(input("Digite o nome do jogador: "))
    jogador["partidas"] = int(input("Quantas partidas: "))
    for c in range(1, jogador["partidas"]+1):
        jogador1.append(int(input("Quantos gols na partida {}? ".format(c))))
    jogador['gols'] = jogador1[:]
    jogador['total'] = sum(jogador1)
    time.append(jogador.copy())
    resp = str(input("Deseja continuar? [S/N]: "))

print(f'Cod ', end='')
print(f'Nome', end='       ')
print(f'Partidas', end='   ')
print(f'Gols', end='       ')
print(f'Total')
print('-' *50)
for k, v in enumerate(time):
    print(f'{k:<3}', end=' ')
    for d in v.values():
        print(f'{str(d):<10}', end=' ')
    print()
print('-'*50)
while True:
    busca = int(input("Mostrar qual jogador 999-Encerra: "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Erro...")
    else:
        print(f" -- Levantamento do jogador {time[busca]['nome']}")
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols...')
    print('-'*50)
print('Encerrando...')
