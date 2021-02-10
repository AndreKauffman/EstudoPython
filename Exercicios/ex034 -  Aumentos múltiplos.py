salario = float(input("Digite seu salario: "))

salarioporcentagem15 = salario  * 15 / 100
salarioporcentagem10 = salario * 10 / 100

if salario > 1250:
   salario1 = salarioporcentagem10 + salario
   print("seu salario de {} é um novo salario {}".format(salario, salario1))
else:
   salario1 = salario + salarioporcentagem15
   print("seu salario de {} é um novo salario {}".format(salario, salario1))
