cont = 0
a = 0
for c in range(1,500,2):
    if c % 3 == 0:
        cont = cont + 1
        a = a + c
print("a soma é {}".format(a))
print("{}".format(cont))

