nome = str(input("qual é seu nome: "))
if nome == 'andre':
    print("que nome bonito!")
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print("seu nome é bem popular")
elif nome in 'ana claudia jessica juliana marta':
    print("que nome feminino lindo")
else:
    print("seu nome é bem normal!")
print("tenha um bom dia {}".format(nome))