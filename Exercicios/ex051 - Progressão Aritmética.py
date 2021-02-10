termo = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = termo + (10 - 1) * razão
for c in range(termo,decimo + razão,razão):
    print('{}'.format(c), end=" -> ")
print("ACABOU")