matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = soma = soma1 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
print('-=' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma = soma + matriz[linha][coluna]
    print()
print('=-' * 30)
print(f"A soma dos pares é igual a {soma}...")
print(f"O maior valor da segunda coluna é {max(matriz[1])}".format())

for cada in matriz[2]:
    soma1 = soma1 + cada
print(f"A soma dos valores da terceira coluna é {soma1}")