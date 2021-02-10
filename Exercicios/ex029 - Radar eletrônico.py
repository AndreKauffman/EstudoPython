from time import sleep
vel = int(input("Digite a velocidade: "))
sleep(1)
if vel > 80:
    print("Multado!!!")
    num1 = (vel - 80) * 7
    print("Voce deve pagar uma multa de R${:.2f}".format(num1))
print("tenha um BOM DIA!")