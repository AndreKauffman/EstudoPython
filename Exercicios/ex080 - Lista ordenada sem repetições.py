# MINHA SOLUÇÃO
'''valores = []
maior = menor = meio =0
cont = 0
for valor in range(1,6):
    num = int(input("Digite um valor:" ))
    valores.append(num)
    if cont == 0:
        print("Valor adicionado ao final da lista...")
        maior = menor = meio = num
    else:
        if num > maior:
            print("Valor adicionado ao final da lista...")
            maior = num
        if num < menor:
            print("Valor adicionado na posição 0 da lista...")
            menor = num
        if num < maior and num > menor:
            print("Valor adicionado na posição 1 da lista...")
            meio = num
    cont+=1
valores.sort()
print(f"Os valores digitados em ordem foram {valores}")'''

# CERTA

valores = []
for c in range(0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print(f"Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f"Adcionado na posição {pos} da lista...")
                break
            pos+=1
print("-=" * 30)
print(f"Os valores digitados foram {valores}")

