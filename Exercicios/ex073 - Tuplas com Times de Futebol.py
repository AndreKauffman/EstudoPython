times = 'São Paulo', 'Corinthias', 'PaLmeiras', 'Santos', 'Atl.Mineiro', "Real", 'Barcelona', 'Atl.Madrid', 'Milan', 'Bayern'
print('-='*8)
print("Lista de Times: {}".format(times))
print('-='*8)
print("Os cinco primeiros são {}".format(times[0:5]))
print('-='*8)
print("Os quatro ultimos são {}".format(times[6:]))
print('-='*8)
print('Em ordem alfabetica são: {}'.format(sorted(times)))
print('-='*8)
print(f"O Barcelona está na {times.index('Barcelona')+1}° posição")