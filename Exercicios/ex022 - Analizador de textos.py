nome = str(input("Digite seu nome completo: ")).strip()
print("Analizando......... ")
dividido = nome.split()
print("Seu nome em maiusculas é {}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print("Seu nome em maiusculas é {}".format(len(nome)-nome.count(' ')))
print("Seu nome em maiusculas é {}".format(dividido[0]))