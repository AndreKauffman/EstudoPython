dados = {}
from datetime import datetime
dados["nome"] = str(input("Nome: "))
dados['ano'] = int(input("Ano de nascimento: "))
data = datetime.now().year - dados['ano']
dados['ctps'] = int(input("CTPS (0 se não tem): "))
if dados['ctps'] == 0:
    print('-' * 30)
    print(f'  - Nome tem o valor {dados["nome"]}')
    print(f'  - Idade tem o valor {data}')
    print(f"  - CTPS tem o valor {dados['ctps']}")
else:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salario: R$"))
    dados['apos'] = dados['ano'] + ((dados['contratação'] + 35) - datetime.now().year)
    print('-' * 30)
    print(f'  - Nome tem o valor {dados["nome"]}')
    print(f'  - Idade tem o valor {data}')
    print(f'  - CTPS tem o valor {dados["ctps"]}')
    print(f'  - Contratação tem o valor {dados["contratação"]}')
    print(f'  - Salario tem o valor R${dados["salario"]}')
    print(f'  - Aposentadoria tem o valor: Em {dados["apos"]}')

