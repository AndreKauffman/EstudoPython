palavra = ('Andre', 'Lidia', 'Antonio', 'Victoria')

for n in palavra:
    print("\nNa palavra {} temos: ".format(n.upper()), end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra,end='')