from time import sleep
def valores(*numeros):

    print('-'*30)
    print("Analizando os valores...")

    i = 0
    while i != len(numeros):
        print(f'{numeros[i]} ', end='', flush=True)
        sleep(0.5)
        i += 1
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {max(numeros)}.')


#PP
valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores(0)
