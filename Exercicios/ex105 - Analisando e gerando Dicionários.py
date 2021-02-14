''' MEU PROGRAMA

def notas(*num, sit=False):
    ''''''
    :param num: Recebe notas de uma aluno.
    :param sit: As notas a serem analizadas
    :return: UM print com as notas e a situação
    ''''''
    a = 0
    soma = 0
    for c in num:
        a+=1
        soma = soma + c
    soma1 = soma / a

    print('{', end=' ')
    print(f'Total: {a}', end=', ')
    print(f'Maior = {max(num)}', end=', ')
    print(f'Menor = {min(num)}', end=', ')
    print(f"Media: {soma1}", end=', ')
    if sit == True:
        if soma1 > 5:
            print("Situação: Aprovado", end='. ')
        else:
            print('Situação: Reprovado', end='. ')
    print('}')


notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)'''
def notas(*num, sit=False):
    """
    :param num: Calcula as notas dos alunos
    :param sit: Caso queira ver a situação
    :return: um dicionario com as notas e situação
    """
    d = dict()
    d['Total'] = len(num)
    d['Maior'] = max(num)
    d['Menor'] = min(num)
    d['Media'] = sum(num)/len(num)
    if sit == True:
        if d['Media'] > 5:
            d['Situação'] = 'Aprovado'
        else:
            d['Situação'] = 'Reprovado'
    return d


#PP
resp = notas(5.5, 2.5, 9, 8.5)
print(resp)
help(notas)


