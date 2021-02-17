def metade(n = 0, formato = False):
    resp = n / 2
    return resp if formato is False else m(resp)


def dobro(n = 0, formato = False):
    resp = n * 2
    return resp if formato is False else m(resp)


def aumentar(n = 0, p = 0, formato = False):
    valor = n * p / 100
    resp = valor + n
    return resp if formato is False else m(resp)


def diminuir(n = 0, p = 0, formato = False):
    valor = n * p / 100
    resp = n - valor
    return resp if formato is False else m(resp)


def m(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, aumento = 1, redução = 1):
    print(f'-' * 40)
    print(f'          RESUMO DO VALOR')
    print(f'-' * 40)
    print(f'A metade de R${preco:.2f} é: \t{metade(preco, True)}'.replace('.', ','))
    print(f'O dobro de R${preco:.2f} é: \t{dobro(preco, True)}'.replace('.', ','))
    print(f'Aumentando {aumento}%, Temos: \t\t{aumentar(preco, aumento, True)}')
    print(f'Diminuindo {redução}%, Temos: \t\t{diminuir(preco, redução, True)}')
    print(f'-'*40)
