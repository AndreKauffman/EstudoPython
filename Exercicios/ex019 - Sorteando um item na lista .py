import random
alunos = str(input("Primeiro aluno: "))
alunos2 = str(input("segundo aluno: "))
alunos3 = str(input("terceiro aluno: "))
alunos4 = str(input("quarto aluno: "))
alunos5 = str(input("quinto aluno: "))
lista = [alunos, alunos2, alunos3, alunos4, alunos5]
escolhido = random.choice(lista)
print("O aluno foi {}".format(escolhido))