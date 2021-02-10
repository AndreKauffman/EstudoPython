frase = str(input("Digiote uma frase: ")).strip()
print("A letra A aparece {} vezes".format(frase.upper().count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.upper().find('A')+1))
print("A ultima letra A apareceu na posição {}".format(frase.upper().rfind('A')+1))

# .RFIND PROCURA DO FIM PRO COMEÇO