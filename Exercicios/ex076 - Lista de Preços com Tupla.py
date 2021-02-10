lista = ('Lápiz',1.75,
          'Borracha',2,
          'Caderno',15,
          'Estojo',25,
          'Transferidor',4.20
         )
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":40}')
print('-'*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>6.2f}')
print('-'*40)