alugueld = int(input("DIgite os dias: "))
km = float(input("DIgite os km rodados: "))
dias = alugueld * 60
horas = km * 0.15
total = dias + horas
print("Voce pagará R${} por {} dias e {} km rodados".format(total, alugueld, km))