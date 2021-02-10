num = int(input("Digite um numero inteiro: "))
print("""Escolha umas das bases
[ 1 ] = Binario
[ 2 ] = Octal
[ 3 ] = Hexadecimal""")

opcao = int(input("Sua opção:"))

if opcao == 1:
    print("{} convertido para binario é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
else:
    print("{} convertido para Hexa é igual a {}".format(num, hex(num)[2:]))