num = (int(input("Digite um numero: ")),
      int(input("Digite outro numero: ")),
      int(input("Digite mais um numero: ")),
      int(input("Digite o ultimo numero: ")))
print("Voce digitou os valores {}".format(num))
print("O valor 9 apareceu {} vezes".format(num.count(9)))
if 3 not in num:
    print("O valor 3 não apareceu")
else:
    print("O valor 3 apareceu na posição {}°".format(num.index(3)+1))
print("Os valores pares digitados foram", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')