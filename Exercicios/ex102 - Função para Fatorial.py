def fatorial(num, show=False):
    '''
            -> Testando help
    :param num: Numero a ser calculado...
    :param show: caso queira ver a conta...
    :return: O valor faltorial do numero num
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)

