import random
def sorteio(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0,5):
        num = random.randint(1,10)
        lista.append(num)
        print(f'{num}', end=' ')

def somar(num1):
    print()
    print(f'Somando os pares de {numeros}, temos', end=' ')
    s = 0
    for valor in numeros:
        if valor % 2 == 0:
            s = s + valor
    print(f'{s}')

numeros = list()
sorteio(numeros)
somar(numeros)
print()

