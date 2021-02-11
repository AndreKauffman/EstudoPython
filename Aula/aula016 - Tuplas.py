lanche = 'hamburguer', 'suco', 'pizza', 'pudim'

for comida in lanche:
    print(f"Eu vou comer {comida}")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")

for posição, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {posição}")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")


