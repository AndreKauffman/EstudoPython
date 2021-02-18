import time
#   MINHAS FUNÇÕES
def menu():
    print('-' * 40)
    print('             MENU PRINCIPAL')
    print('-' * 40)
    print('''1 - Ver pessoas Cadastradas.
2 - Cadastrar nova pessoa.
3 - Sair''')
    print('-' * 40)


def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro... 0 pessoas cadastradas!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')
    finally:
        a.close()


def arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro..')
    else:
        print(f'arquivo {arq} foi Criado...')


def cadastro(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print("Não consegui abrir o arquivo...")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro...')
        else:
            print(f'Novo registro de {nome}')


# PROGRAMA PRINCIPAL:
arq = 'Cadastro.txt'
resp = 0
r = 's'


while True:

    #CASO A RESP FOR 3 O PROGRAMA FINALIZA
    if resp == 3:
        break

    #ABRE O MENU
    menu()

    #VALIDAÇÃO DA RESP
    try:
        resp = int(input('Sua opção: '))
    except:
        print('Erro... Digite uma opção válida!')

    # MOSTRA AS PESSOAS CADASTRADAS
    if resp == 1:
        time.sleep(2)
        print('-' * 40)
        print('               CADASTRADOS')
        print('-' *40)
        ler(arq)

    #CRIA A PASTA SE NÃO TEM E MOSTRA AS PESSOAS
    if resp == 2:
        time.sleep(2)
        print('-' * 40)
        print('               NOVO CADASTRO')
        print('-' * 40)
        if not arquivo(arq):
            criar(arq)
    if resp == 2:
        while True:
            if r == 'n':
                break
            print('Novo Cadastro... ')
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            cadastro(arq, nome, idade)
            r = str(input('Quer cadastrar mais uma? [S/N]'))

print('-' * 40)
print('Saindo do sistema, até logo...')
print('-' * 40)

