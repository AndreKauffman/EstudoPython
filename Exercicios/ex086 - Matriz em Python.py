'''
a = 0
b = 0
c = 0
d = 2
e = 1
i = 0
num = 0
h = 0
valores = []
num = [[], [], [], [], [], [], [], [], []]
for c in range(0, 1):
    while a <= 2:
        valores.append(int(input(f"Digite um valor {b, a}: ")))
        num.append(num[i])
        a += 1
        i+=1
    while b <= 2:
        valores.append(int(input(f"Digite um valor {e, b}: ")))
        num.append(num[i])
        b += 1
        i += 1
    while c <= 2:
        valores.append(int(input(f"Digite um valor {d, c}: ")))
        num.append(num[i])
        c+=1
        i += 1
print('-=' * 30)

for h in range(0,3):
    print(f"[ {valores[h]} ]", end=' ')
    h+=1
print()
for h in range(3,6):
    print(f"[ {valores[h]} ]", end=' ')
    h+=1
print()
for h in range(6, 9):
    print(f"[ {valores[h]} ]", end=' ')'''

# CERTA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
print('-=' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
