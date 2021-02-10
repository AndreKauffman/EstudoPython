price = float(input("qual o preço do produto? "))
discount = int(input("qual o desconto? "))
porcent = (price * discount) / 100
value = price - porcent
print("O valor do produto que custa {} com {}% de desconto fica {}".format(price, discount, value))
