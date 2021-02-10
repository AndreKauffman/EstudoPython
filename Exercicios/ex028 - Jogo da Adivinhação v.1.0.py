import random
from time import sleep
print("Advinhe o numero de 0-5 que pensei!!!")
num = int(input("Digite um numero: "))
sleep(3)
num1 = random.randint(0,5)

if num == num1:
    print("voce acertou, foi o numero {}!!".format(num1))
else:
    print("errou ruinzão")


