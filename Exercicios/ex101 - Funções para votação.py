def votar(num):
    import datetime
    data = datetime.date.today().year
    idade = data - valor
    if idade >= 18 and idade <= 65:
        print(f'Com {idade} anos, o voto é Obrigatorio...')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade} anos, o voto é opicional...')
    else:
        print(f'Com {idade} anos, Não vota...')


valor = int(input('Em que ano você nasceu: '))
votar(valor)