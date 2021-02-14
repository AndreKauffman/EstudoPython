def jogador(player= '<desconhecido>', gols = 0):
    print(f"O jogador {player} fez {gols} gols na partida...")

nome = str(input("Nome: "))
gol = str(input("Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    jogador(gols = gol)
else:
    jogador(nome, gol)

