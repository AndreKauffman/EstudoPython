def contador(i,f,p):
    print('-'*30)
    print(f'Contagem de {i} até o {f} de {p} em {p}')

    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont+=p
        print("Fim...")
        print('-'*30)
    elif i >= f:
       cont = i
       while cont >= f:
           print(f'{cont}', end=' ')
           cont -= p
       print("Fim...")
       print('-' * 30)

#PP
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passos = int(input("Passos: "))
contador(inicio, fim, passos)
