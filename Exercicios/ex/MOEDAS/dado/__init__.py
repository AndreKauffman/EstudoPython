def validar(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f"ERRO...{entrada} não é um valor valido...")
        else:
            valido = True
            return float(entrada)


