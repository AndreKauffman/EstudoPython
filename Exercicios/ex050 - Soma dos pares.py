a = 0
cont = 0
for c in range(0,6):
    num = int(input("Quais numeros?"))
    if num % 2 == 0:
        a = a + num
        cont = cont + 1
print(a)