aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = int(input("Media: "))
print('-' * 30)
print(f'Nome é igual a {aluno["nome"]}')
print(f'Media é igual a {aluno["media"]}')
if aluno['media'] < 5:
    print("A situação é Reprovado!")
elif aluno['media'] > 5 and aluno['media'] < 7:
    print("A situação é Recuperação ")
else:
    print("A situação é Aprovado")