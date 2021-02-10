import math
ca = float(input("Digite o cateto adjacente: "))
co = float(input("Digite o cateto oposto: "))
hi = math.hypot(ca, co)
print("O valor da hipotenusa é {}".format(hi))