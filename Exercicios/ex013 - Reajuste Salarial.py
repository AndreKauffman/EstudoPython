salary = float(input("qual o salario? "))
increase = int(input("qual o aumento? "))
porcent = (salary * increase) / 100
value = salary + porcent
print("O salario que era {} com {}% de aumento fica {}".format(salary, increase, value))
