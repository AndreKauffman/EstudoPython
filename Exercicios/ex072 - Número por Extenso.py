num = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
valor = int(input("Digite um valor entre 0 e 20: "))
while valor > 20 or valor < 0:
    valor = int(input("Tente novamente. Digite um valor entre 0 e 20"))
print("Voce digitou o numero {}".format(num[valor]))