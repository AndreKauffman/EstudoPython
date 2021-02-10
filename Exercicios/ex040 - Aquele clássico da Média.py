nota = float(input("Digite sua nota: "))
nota1 = float(input("Digite outra nota: "))
soma = (nota + nota1) / 2

if soma >= 6:
    print("o aluno foi aprovado com a nota {}".format(soma))
elif soma == 5:
    print("o aluno esta de recuperação com a nota {}".format(soma))
else:
    print("o aluno reprovou com a nota {}".format(soma))