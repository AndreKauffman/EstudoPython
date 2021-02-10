import random
from time import sleep
lista = list()
jogos = list()
print("-=" * 15)
print(f"      Jogo da MegaSena     ")
print("-=" * 15)
quant = int(input("Quantos jogos? "))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

print('-=' * 4, '> BOA SORTE <', '-=' * 4)
