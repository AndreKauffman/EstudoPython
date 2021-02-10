'''import math
num = int(input("Digite um numero pra ver seu fatorial: "))
fact = math.factorial(num)
print("O fatorial de {} é {}".format(num, fact))'''

'''num = int(input("Digite um numero pra ver seu fatorial: "))
cont = num
f = 1
print("calculando {}!".format(num), end=' ')
while cont > 0:
    print("{}".format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f)'''

num = int(input("Digite um numero pra ver seu fatorial: "))
cont = num
fatorial = 1
for num in range(num, 0, -1):
    print('{}'.format(num), end=" ")
    print('x ' if num > 1 else '= ', end='')
    fatorial = num * fatorial
print(fatorial, end='')

