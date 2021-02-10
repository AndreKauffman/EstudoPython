import random
alunos = str(input("Primeiro aluno: "))
alunos2 = str(input("segundo aluno: "))
alunos3 = str(input("terceiro aluno: "))
alunos4 = str(input("quarto aluno: "))
lista = [alunos, alunos2, alunos3, alunos4]
random.shuffle(lista)
print("A ordem é {}".format(lista))