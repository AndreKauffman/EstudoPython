viagem = float(input("Digite a longitude da viagem em KM: "))
if viagem > 200:
    viagem1 = viagem * 0.45
    print("voce pagará R${} por {} KM".format(viagem1, viagem))
else:
    viagem1 = viagem * 0.50
    print("voce pagará R${} por {} KM".format(viagem1, viagem))
