from time import sleep
alunos = []
alunos1 = []

while True:
    nome = str(input("Nome: "))
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append(nome)
    alunos.append(media)
    alunos1.append(alunos[:])
    alunos.clear()
    resp = str(input("Deseja continuar? [S/N]: "))
    if resp == 'n':
        break

print('--' * 15)
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
for i,l in enumerate(alunos1):
    print(f'{i:<4}{l[0]:10}{l[1]:>8.1f}')
print('-' * 30)

while True:
    opcao = int(input("Mostrar as notas dos aluno? (999 interrompe!): "))
    if opcao <= len(alunos1) -1 :
        print(f'a media de {alunos1[opcao][0]} é {alunos1[opcao][1]}')
        print('-' * 30)
    if opcao == 999:
        break



