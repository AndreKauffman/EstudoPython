def leia(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("\033[0;31mERRO!! Digite um valor correto!!!\033[m")
    return valor

#PP
n = leia("Digite um numero: ")
print(f"Voçê digitou o numero {n}...")
