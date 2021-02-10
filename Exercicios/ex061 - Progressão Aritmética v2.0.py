termo = int(input("Termo: "))
razão = int(input("Razão: "))
primeiro = termo
cont = 1
while cont <= 10:
    print("{} -> ".format(primeiro),  end="")
    primeiro += razão
    cont+=1
print("fim")