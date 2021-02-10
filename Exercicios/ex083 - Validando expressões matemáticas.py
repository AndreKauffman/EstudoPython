frase = str(input("Digite a expressão: ")).strip()
if frase.count('(') == frase.count(')'):
    print("Sua expressão é valida...")
else:
    print("Sua expressão não é valida...")