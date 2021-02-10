a = int(input("Digite um valor: "))
b = int(input("Digite o segundo: "))
c = int(input("Digite o terceiro valor: "))

menor = a
if b < a and b < c:
   menor = b
if c < a and c < b:
   menor = c

maior = a
if b > a and b > c:
   maior = b
if c > a and c > b:
   maior = c

print("o menor {}".format(menor))
print("o maior {}".format(maior))

