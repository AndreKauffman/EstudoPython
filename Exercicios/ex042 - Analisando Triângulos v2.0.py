lado1 = float(input("Digite um lado do triangulo: "))
lado2 = float(input("Digite um outro lado do triangulo: "))
lado3 = float(input("Digite um outro lado do triangulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Formam um triangulo.....")
    if lado1 == lado2 == lado3:
        print("é um triangulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("é um triangulo isósceles")
    else:
        print("é um triangulo escaleno")
else:
    print("Não pode formar")


