def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um numero: "))
print(f"O fatorial de {n} é {fatorial(n)}")

print('-' * 100)

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um valor: "))
if par(num):
    print("par")
else:
    print("Não é")