valores = []
maior = menor = 0
for v in range(0,5):
    valores.append(int(input("Digite um valor: ")))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            valores = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('-='*30)
print(f"Voce digitou os valores {valores}")
print(f"o maior valor digitado foi {maior} nas posições: ", end=' ')
for i, w in enumerate(valores):
    if w == maior:
        print(f"{i}...", end=" ")
print(f"\no menor valor digitado foi {menor} nas posições: ", end=' ')
for i,w in enumerate(valores):
    if w == menor:
        print(f"{i}...",end=' ')
