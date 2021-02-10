peso = float(input("Digite seu peso (KG): "))
alt = float(input("Digite sua altura: (M)"))
somalt = alt * 2
somapeso = peso / somalt

if somapeso < 18.5:
    print("seu IMC é {:.1f}, voce está abaixo do peso!".format(somapeso))
elif somapeso >= 18.5:
    print("seu IMC é {:.1f}, voce está no peso normal!".format(somapeso))
elif somapeso >= 24.9:
    print("seu IMC é {:.1f}, voce está acima do peso!".format(somapeso))
elif somapeso >= 29.9:
    print("seu IMC é {:.1f}, voce está abaixo do peso!".format(somapeso))
elif somapeso >= 34.9:
    print("seu IMC é {:.1f}, voce está abaixo do peso!".format(somapeso))
elif somapeso > 39.9:
    print("seu IMC é {:.1f}, voce esta em obesidade grau 3".format(somapeso))