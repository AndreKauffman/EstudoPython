termo = int(input("Termo: "))
razão = int(input("Razão: "))
primeiro = termo
cont = 1
mais = 10
total = 0
a = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(primeiro),  end="")
        primeiro += razão
        cont+=1
        a+=1
    mais = int(input("Digite quantos termos a mais voce quer ver"))
print("FIM")
print("Ao todo foi mostrado {} de termos".format(total))


